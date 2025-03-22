import logging
from collections import defaultdict

import recap_argument_graph as ag
from recap_am.model.config import config
from recap_am.relation.controller import mc_from_relations
from recap_am.relation.controller.attack_support import (
    _load_model,
    _predict,
    _transform,
)
from recap_am.relation.model.relation import Relation, RelationClass


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
    mc_node = ag.Node(
        key=graph.keygen(), text=str(mc), category=ag.NodeCategory.I, major_claim=True
    )
    graph.add_node(mc_node)
    outer_adus = [a for a in adus if not a == mc]
    for adu in outer_adus:
        cnode = ag.Node(key=graph.keygen(), text=str(adu), category=ag.NodeCategory.I)
        if relations[adu][mc].classification == RelationClass.ATTACK:
            snode = ag.Node(
                key=graph.keygen(), text="Default Conflict", category=ag.NodeCategory.CA
            )
        else:
            snode = ag.Node(
                key=graph.keygen(),
                text="Default Inference",
                category=ag.NodeCategory.RA,
            )

        logging.debug("Match")
        graph.add_edge(ag.Edge(key=graph.keygen(), start=cnode, end=snode))
        graph.add_edge(ag.Edge(key=graph.keygen(), start=snode, end=mc_node))
    return graph
