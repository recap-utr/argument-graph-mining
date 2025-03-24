import logging

import arguebuf as ag
import edlib

from argmining.model.config import config

logger = logging.getLogger(__name__)


# def _jaccard(node1: ag.Node, node2: ag.Node) -> float:
#     return 1 - nltk.jaccard_distance(
#         {t.text for t in node1.text}, {t.text for t in node2.text}
#     )


def _edit(node1: ag.AtomNode, node2: ag.AtomNode) -> float:
    # distance = nltk.edit_distance(node1.raw_text, node2.raw_text)
    distance = edlib.align(node1.plain_text, node2.plain_text)["editDistance"]

    return 1 - (distance / max(len(node1.plain_text), len(node2.plain_text)))


def _exact(node1: ag.AtomNode, node2: ag.AtomNode) -> float:
    return 1.0 if node1.plain_text == node2.plain_text else 0.0


def nodes(node1: ag.AbstractNode, node2: ag.AbstractNode) -> float:
    switch = {
        # "jaccard": _jaccard,
        "edit": _edit,
        "exact": _exact,
    }

    if type(node1) is type(node2):
        if type(node1) is ag.AtomNode and type(node2) is ag.AtomNode:
            if node1.plain_text == node2.plain_text:
                return 1.0
            else:
                return switch[config["evaluation"]["similarity"]](node1, node2)
        else:
            return 1.0

    return 0.0


def edges(edge1: ag.Edge, edge2: ag.Edge) -> float:
    return 0.5 * (nodes(edge1.source, edge2.source) + nodes(edge1.target, edge2.target))
