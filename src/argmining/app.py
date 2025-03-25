from __future__ import absolute_import, annotations

import io
import logging
import multiprocessing
import os
import traceback
import typing as t
import warnings
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from timeit import default_timer as timer
from zipfile import ZipFile

import flask
import grpc
import pendulum
from grpc_reflection.v1alpha import reflection
from sklearn.model_selection import ParameterGrid
from werkzeug.datastructures import FileStorage

import arggraph as ag
from arg_services.graph.v1 import graph_pb2
from arg_services.mining.v1beta import mining_pb2, mining_pb2_grpc
from argmining.adu import run_task
from argmining.controller.preprocess import prep_production
from argmining.evaluation import evaluator
from argmining.model.config import config
from argmining.model.protobuf_graph import aif2protobuf
from argmining.model.query import Query
from argmining.model.statistic import Statistic, Statistics
from argmining.relation import construct_graph
from argmining.relation.controller import attack_support

logging.basicConfig(level=logging.WARNING)

log = logging.getLogger(__package__)
log.setLevel(logging.INFO)

warnings.filterwarnings("ignore")


def run_server() -> None:
    """Start a flask server."""

    app = flask.Flask(__package__, root_path=str(Path(__file__).resolve().parent))
    app.config.update(TEMPLATES_AUTO_RELOAD=True, FLASK_ENV="development")
    app.secret_key = os.urandom(16)

    @app.route("/", methods=["POST", "GET"])
    def index():
        stats = None

        if flask.request.method == "POST":
            try:
                query_files = flask.request.files.getlist("query-files")  # pyright: ignore
                _update_config(flask.request.form, from_flask=True)  # pyright: ignore
                stats = run(query_files)
            except Exception:
                flask.flash(traceback.format_exc(), "error")

        return flask.render_template("index.html", config=config, statistics=stats)

    @app.route("/download/<folder>")
    def download(folder):
        out_path = Path(config["path"]["output"], folder)

        if out_path.exists():
            data = io.BytesIO()

            with ZipFile(data, mode="w") as z:
                for file in out_path.iterdir():
                    z.write(file, file.name)

            data.seek(0)
            # shutil.rmtree(out_path)

            return flask.send_file(
                data,
                mimetype="application/zip",
                as_attachment=True,
                attachment_filename=f"{folder}.zip",
            )

        flask.flash("The requested file is not available.", "error")
        return flask.render_template("index.html", config=config, statistics=None)

    app.run(host=config["flask"]["host"], port=config["flask"]["port"])


def evaluate() -> None:
    param_grid = {
        "mc-method": ["centroid", "first", "pairwise", "relations"],
        "relation-threshold": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "relation-method": ["adu_position", "flat_tree", "pairwise_comparison"],
    }
    grid = ParameterGrid(param_grid)
    timestamp = _timestamp()

    params = [(grid_entry, timestamp) for grid_entry in grid]

    if config["debug"]:
        for param in params:
            _single_eval(*param)

    else:
        with multiprocessing.Pool() as pool:
            pool.starmap(_single_eval, params)


def _single_eval(params: t.Mapping[str, t.Any], timestamp: str) -> None:
    log.info(f"Evaluating with params: {params}")
    _update_config(params)

    run(
        timestamp=timestamp,
        subfolder="-".join((str(value) for value in params.values())),
    )


def _timestamp() -> str:
    return pendulum.now().format("YYYY-MM-DD-HH-mm-ss")


def run(
    query_files: t.Optional[t.List[FileStorage]] = None,
    timestamp: t.Optional[str] = None,
    subfolder: t.Optional[str] = None,
) -> Statistics:
    """Run the argument mining process."""

    if not timestamp:
        timestamp = _timestamp()

    out_path = Path(config["path"]["output"], timestamp)

    if subfolder:
        out_path = out_path / subfolder

    out_path.mkdir(parents=True)
    stats = Statistics(timestamp)

    log.info("Loading documents.")
    start_time = timer()

    queries = Query.from_flask(query_files) or Query.from_folder(
        Path(config["path"]["input"])
    )

    for i, query in enumerate(queries):
        log.info(f"Processing '{query.name}' ({i + 1}/{len(queries)}).")

        stat = stats.new(query)

        try:
            _process_run(query, stat, out_path)
        except Exception:
            print(traceback.format_exc())

    stats.duration = timer() - start_time
    stats.save(out_path)

    log.info("Done.")

    return stats


def _text2graph(name: str, text: str) -> ag.Graph:
    """Do the processing for one input file."""

    # Preprocessing
    doc = prep_production(name, text)

    # ADU classification
    doc = run_task.run_production(doc)

    # Attack/support classification
    rel_types = attack_support.classify(doc._.ADU_Sents)

    # Create graph with relationships
    return construct_graph.main(doc, rel_types)


def _process_run(query: Query, statistic: Statistic, out_path: Path) -> None:
    """Do the processing for one input file."""

    start_time = timer()

    # Preprocessing
    doc = prep_production(query.name, query.text)

    # ADU classification
    doc = run_task.run_production(doc)

    # Attack/support classification
    rel_types = attack_support.classify(doc._.ADU_Sents)

    # Create graph with relationships
    graph_end2end = construct_graph.main(doc, rel_types)

    statistic.duration = timer() - start_time

    _export(graph_end2end, out_path, "end2end")

    if query.benchmark:
        graph_preset = evaluator.run(
            statistic, doc, rel_types, graph_end2end, query.benchmark
        )
        _export(graph_preset, out_path, "preset")

    statistic.save(out_path)


def _export(graph: ag.Graph, folder: Path, suffix: str = "") -> None:
    """Export a graph according to settings in `config`."""

    if config["export"]["json"]:
        graph.save(folder / f"{graph.name}-{suffix}.json")

    if config["export"]["picture"]:
        graph.render(folder / f"{graph.name}-{suffix}.pdf")


def _update_config(data: t.Mapping[str, t.Any], from_flask: bool = False) -> None:
    """Contents of `config.toml` is updated according to web request.

    This only works with options that can be changed without reloading the whole program.
    For example, it is not possible to change the language model as it is only loaded once during initialization.
    """

    if from_flask:
        config["export"]["json"] = bool(data.get("export-json"))
        config["export"]["picture"] = bool(data.get("export-picture"))
        config["path"]["input"] = data["input-path"]

    if "relation-fallback" in data:
        config["relation"]["fallback"] = data["relation-fallback"]
    if "mc-method" in data:
        config["adu"]["MC"]["method"] = data["mc-method"]
    if "relation-method" in data:
        config["relation"]["method"] = data["relation-method"]
    if "relation-threshold" in data:
        config["relation"]["threshold"] = float(data["relation-threshold"])


class MiningService(mining_pb2_grpc.MiningServiceServicer):
    def RunPipeline(self, request, context):
        response = mining_pb2.RunPipelineResponse()
        _update_config(request.extras)

        for idx, text in enumerate(request.texts, start=1):
            log.info(f"Processing {idx}/{len(request.texts)}.")

            try:
                graph_aif = _text2graph(str(idx), text)
                graph_pb = aif2protobuf(graph_aif)
                response.graphs.append(graph_pb)  # pyright: ignore
            except Exception:
                print(traceback.format_exc())
                response.graphs.append(graph_pb2.Graph())  # pyright: ignore

        return response


def run_grpc():
    address = f"{config['grpc']['host']}:{config['grpc']['port']}"
    server = grpc.server(ThreadPoolExecutor(max_workers=1))
    mining_pb2_grpc.add_MiningServiceServicer_to_server(MiningService(), server)

    reflection.enable_server_reflection(
        [
            mining_pb2.DESCRIPTOR.services_by_name["MiningService"].full_name,
            reflection.SERVICE_NAME,
        ],
        server,
    )

    server.add_insecure_port(address)
    server.start()

    print(f"Listening on {address}.")
    server.wait_for_termination()
