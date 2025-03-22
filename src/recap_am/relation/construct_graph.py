import typing as t

from spacy.tokens.doc import Doc

from recap_am.model.config import config
from recap_am.relation.controller import adu_position, flat_tree, pairwise_comparison


def main(doc: Doc, relations: t.Any, preset_mc: bool = False):
    method = config["relation"]["method"]

    if method == "adu_position":
        return adu_position.run(doc, relations, preset_mc)

    elif method == "pairwise_comparison":
        return pairwise_comparison.run(doc, preset_mc)

    elif method == "flat_tree":
        return flat_tree.run(doc, preset_mc)

    raise ValueError("Wrong config value for 'relation.method'.")
