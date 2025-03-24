import logging
from collections import defaultdict

import arguebuf as ag

from argmining.model.config import config
from argmining.relation.controller import mc_from_relations
from argmining.relation.controller.attack_support import (
    _load_model,
    _predict,
    _transform,
)
from argmining.relation.model.relation import Relation, RelationClass


def compare_all(adus, mc):
    """Compute classification for all ADU Pairs."""
    model = _load_model()
    relations = defaultdict(dict)
    for adu in adus:
        sample = _transform(adu, mc)
        pred_type, pred_prob = _predict(sample, model)
        relations[adu][mc] = Relation(mc, pred_prob, pred_type)
        relations[adu]["main"] = relations[adu][mc]
        for adu2 in adus:
            if adu == adu2 or adu2 == mc:
                pass
            else:
                sample = _transform(adu, adu2)
                pred_type, pred_prob = _predict(sample, model)
                relations[adu][adu2] = Relation(adu2, pred_prob, pred_type)
                if (
                    relations[adu][adu2].probability
                    > relations[adu]["main"].probability
                ):
                    relations[adu]["main"] = relations[adu][adu2]
    return relations


connections = defaultdict(dict)


def run(doc, preset_mc: bool):
    """Create Graph through classfication values."""
    mc = doc._.MajorClaim
    adus = doc._.ADU_Sents
    relations = compare_all(adus, mc)

    if config["adu"]["MC"]["method"] == "relations" and not preset_mc:
        mc = mc_from_relations.run_spacy(adus, relations)
        relations = compare_all(adus, mc)

    graph = ag.Graph(name=doc._.key.split("/")[-1])
    mc_node = ag.AtomNode(text=str(mc))
    graph.add_node(mc_node)
    graph.major_claim = mc_node
    outer_adus = [a for a in adus if not a == mc]
    for adu in outer_adus:
        cnode = ag.AtomNode(text=str(adu))
        if relations[adu][mc].classification == RelationClass.ATTACK:
            snode = ag.SchemeNode(ag.Attack.DEFAULT)
        else:
            snode = ag.SchemeNode(ag.Support.DEFAULT)

        logging.debug("Match")
        graph.add_edge(ag.Edge(source=cnode, target=snode))
        graph.add_edge(ag.Edge(source=snode, target=mc_node))
    return graph
