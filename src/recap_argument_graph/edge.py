from __future__ import absolute_import, annotations

import typing as t

import graphviz as gv
import networkx as nx
import pendulum

from . import dt, utils
from .node import Node
from .utils import MISSING, MISSING_TYPE


class Edge:
    """Edge in AIF format."""

    __slots__ = (
        "_key",
        "_start",
        "_end",
        "visible",
        "annotator",
        "date",
    )

    _key: int
    _start: Node
    _end: Node
    visible: t.Optional[bool]
    annotator: t.Optional[str]
    date: t.Optional[pendulum.DateTime]

    def __init__(
        self,
        key: int,
        start: Node,
        end: Node,
        visible: t.Optional[bool] = None,
        annotator: t.Optional[str] = None,
        date: t.Union[MISSING_TYPE, None, pendulum.DateTime] = MISSING,
    ):
        self._key = key
        self._start = start
        self._end = end
        self.visible = visible
        self.annotator = annotator
        self.date = pendulum.now() if date is MISSING else date

        self.__post_init__()

    def __post_init__(self):
        pass

    def __repr__(self):
        return utils.class_repr(
            self, [str(self.key), f"{self.start.plain_text}->{self.end.plain_text}"]
        )

    @property
    def key(self) -> int:
        return self._key

    @property
    def start(self) -> Node:
        return self._start

    @property
    def end(self) -> Node:
        return self._end

    @classmethod
    def from_ova(
        cls,
        obj: t.Any,
        key: int,
        nodes: t.Mapping[int, Node] = None,
        node_class=Node,
        nlp: t.Optional[t.Callable[[str], t.Any]] = None,
    ) -> Edge:
        if not nodes:
            nodes = {}

        start_key = int(obj.get("from").get("id"))
        end_key = int(obj.get("to").get("id"))

        return cls(
            key=key,
            start=nodes.get(start_key) or node_class.from_ova(obj["from"], nlp),
            end=nodes.get(end_key) or node_class.from_ova(obj["to"], nlp),
            visible=obj.get("visible"),
            annotator=obj.get("annotator"),
            date=dt.from_ova(obj.get("date")),
        )

    def to_ova(self) -> t.Dict[str, t.Any]:
        return {
            "from": self.start.to_ova(),
            "to": self.end.to_ova(),
            "visible": self.visible,
            "annotator": self.annotator,
            "date": dt.to_ova(self.date),
        }

    @classmethod
    def from_aif(
        cls,
        obj: t.Any,
        nodes: t.Mapping[int, Node],
        nlp: t.Optional[t.Callable[[str], t.Any]] = None,
    ) -> Edge:
        start_key = int(obj.get("fromID"))
        end_key = int(obj.get("toID"))

        return cls(
            key=int(obj["edgeID"]),
            start=nodes[start_key],
            end=nodes[end_key],
        )

    def to_aif(self) -> t.Dict[str, t.Any]:
        return {
            "edgeID": str(self.key),
            "fromID": str(self.start.key),
            "toID": str(self.end.key),
            "formEdgeID": None,
        }

    def to_nx(self, g: nx.DiGraph) -> None:
        g.add_edge(self.start.key, self.end.key)

    def to_gv(
        self, g: gv.Digraph, color="#666666", prefix: str = "", suffix: str = ""
    ) -> None:
        g.edge(
            f"{prefix}{self.start.key}{suffix}",
            f"{prefix}{self.end.key}{suffix}",
            color=color,
        )

    # def copy(
    #     self, key: int, start: t.Optional[Node] = None, end: t.Optional[Node] = None
    # ) -> Edge:
    #     obj = copy(self)
    #     obj._key = key
    #
    #     if start:
    #         obj._start = start
    #
    #     if end:
    #         obj._end = end
    #
    #     return obj
