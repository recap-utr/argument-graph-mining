from collections.abc import Mapping
import logging
import traceback
import typing as t

import arg_services
import arguebuf as ag
from google.protobuf.struct_pb2 import Struct
import grpc
import typer
from arg_services.graph.v1 import graph_pb2
from arg_services.mining.v1beta import mining_pb2, mining_pb2_grpc

from argmining.adu import run_task
from argmining.controller.preprocess import prep_production
from argmining.relation import construct_graph
from argmining.relation.controller import attack_support
from argmining.model.config import config

log = logging.getLogger(__name__)
app = typer.Typer()


def run_pipeline(name: str, text: str) -> ag.Graph:
    """Do the processing for one input file."""
    # Preprocessing
    doc = prep_production(name, text)

    # ADU classification
    doc = run_task.run_production(doc)

    # Attack/support classification
    rel_types = attack_support.classify(doc._.ADU_Sents)

    # Create graph with relationships
    graph_end2end = construct_graph.main(doc, rel_types)

    return graph_end2end

def update_config(data: Struct) -> None
    if "relation-fallback" in data:
        config["relation"]["fallback"] = data["relation-fallback"]
    if "mc-method" in data:
        config["adu"]["MC"]["method"] = data["mc-method"]
    if "relation-method" in data:
        config["relation"]["method"] = data["relation-method"]
    if "relation-threshold" in data:
        config["relation"]["threshold"] = data["relation-threshold"]

class MiningService(mining_pb2_grpc.MiningServiceServicer):
    def RunPipeline(
        self,
        request: mining_pb2.RunPipelineRequest,
        context: grpc.ServicerContext,
    ) -> mining_pb2.RunPipelineResponse:
        response = mining_pb2.RunPipelineResponse()
        update_config(request.extras)

        for idx, text in enumerate(request.texts, start=1):
            log.info(f"Processing {idx}/{len(request.texts)}).")

            try:
                graph = run_pipeline(str(idx), text)
                graph_pb = ag.dump.protobuf(graph)
                response.graphs.append(graph_pb)
            except Exception:
                print(traceback.format_exc())
                response.graphs.append(graph_pb2.Graph())

        return response


def add_services(server: grpc.Server):
    mining_pb2_grpc.add_MiningServiceServicer_to_server(MiningService(), server)


@app.command()
def start(address: t.Annotated[str, typer.Argument()] = "127.0.0.1:50051"):
    arg_services.serve(
        address,
        add_services,
        [arg_services.full_service_name(mining_pb2, "MiningService")],
    )


if __name__ == "__main__":
    app()
