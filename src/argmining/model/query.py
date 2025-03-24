from __future__ import annotations

import logging
import typing as t
from dataclasses import dataclass
from pathlib import Path

import arguebuf as ag

from argmining.controller import nlp

logger = logging.getLogger(__name__)


extensions = [".json", ".txt", ".text", ".label", ".ann"]


@dataclass(frozen=False, slots=True)
class Query:
    name: str  # File name without suffix
    text: str | None = (
        None  # Content of .txt files, fallbacks: .text file, benchmark.plain_text
    )
    benchmark: ag.Graph | None = None  # Content of .json and .ann files
    _text: str | None = None  # Content of .text files
    _labels: list[str] | None = None  # Labels corresponding to .text files

    @classmethod
    def from_folder(cls, path: Path) -> list[Query]:
        queries: dict[str, Query] = {}

        for ext in extensions:
            for file in sorted(path.rglob(f"*{ext}")):
                name = file.stem
                suffix = file.suffix

                if name not in queries:
                    queries[name] = Query(name)

                with file.open(encoding="utf-8") as f:
                    _parse_file(name, suffix, f, queries[name])

        _postprocess(queries)

        return list(queries.values())


def _postprocess(queries: t.Mapping[str, Query]) -> None:
    for query in queries.values():
        if query._text and not query.text:
            query.text = query._text

        elif query.benchmark and not query.text:
            query.text = next(iter(query.benchmark.resources.values())).plain_text

        if query._text and query._labels and not query.benchmark:
            query.benchmark = _create_graph(query.name, query._text, query._labels)


def _parse_file(name: str, suffix: str, file: t.TextIO, query: Query) -> None:
    if suffix == ".json":
        query.benchmark = _parse_json(name, file)
    elif suffix == ".txt":
        query.text = _parse_txt(file)
    elif suffix == ".text":
        query._text = _parse_txt(file)
    elif suffix == ".label":
        query._labels = _parse_label(file)
    elif suffix == ".ann":
        query.benchmark = _parse_ann(name, file)


def _parse_txt(file: t.TextIO) -> str:
    return file.read()


def _parse_json(name: str, file: t.TextIO) -> ag.Graph:
    return ag.load.json(file, name, ag.load.Config(nlp=nlp.parse))


def _parse_ann(name: str, file: t.TextIO) -> ag.Graph:
    return ag.load.brat(file, name, ag.load.Config(nlp=nlp.parse))


def _parse_label(file: t.TextIO) -> list[str]:
    return file.read().splitlines()


def _create_graph(name: str, text: str, labels: t.Iterable[str]) -> ag.Graph:
    graph = ag.Graph(name)
    doc = nlp.parse(text)
    sents = list(doc.sents)

    for sent, line_label in zip(sents, labels):
        if line_label != "None":
            node = ag.AtomNode(sent)
            graph.add_node(node)

            if line_label == "MajorClaim":
                graph.major_claim = node

    return graph
