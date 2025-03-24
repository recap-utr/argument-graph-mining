import arguebuf as ag
from spacy.tokens import Doc, Span

from argmining.model.config import config
from argmining.relation.controller import mc_from_relations
from argmining.relation.controller.attack_support import (
    Relation,
    RelationClass,
    classify,
)


def run(
    doc: Doc, relations: None | dict[str, list[Relation]], preset_mc: bool
) -> ag.Graph:
    adus = doc._.ADU_Sents
    claims = doc._.Claim_Sents
    premises = doc._.Premise_Sents
    mc = doc._.MajorClaim

    if config["adu"]["MC"]["method"] == "relations" and not preset_mc:
        mc = mc_from_relations.run_str(adus, relations)

    if not relations:
        relations = classify(adus)

    graph = ag.Graph(name=doc._.key.split("/")[-1])
    mc_node = ag.AtomNode(mc)
    cnodes = []
    graph.add_node(mc_node)
    graph.major_claim = mc_node

    for claim in claims:
        if claim != mc:
            cnode = ag.AtomNode(claim)
            snode = _gen_snode(graph, relations[claim.text], mc)

            if snode:
                cnodes.append(cnode)

                graph.add_edge(ag.Edge(source=cnode, target=snode))
                graph.add_edge(ag.Edge(source=snode, target=mc_node))

    for premise in premises:
        if premise != mc:
            pnode = ag.AtomNode(premise)
            match = (mc_node, 0)

            if cnodes:
                scores = {
                    cnode: min(
                        abs(cnode.text.start - pnode.text.end),
                        abs(cnode.text.end - pnode.text.start),
                    )
                    for cnode in cnodes
                }

                min_score = min(scores.values())
                candidates = [
                    node for node, score in scores.items() if score == min_score
                ]

                for candidate in candidates:
                    sim = pnode.text.similarity(candidate.text)
                    if sim > match[1]:
                        match = (candidate, sim)

            snode = _gen_snode(graph, relations[premise.text], match[0].text)

            if snode:
                graph.add_edge(ag.Edge(source=pnode, target=snode))
                graph.add_edge(ag.Edge(source=snode, target=match[0]))

    return graph


def _gen_snode(
    graph: ag.Graph, relations: list[Relation], adu: Span
) -> ag.SchemeNode | None:
    candidates = list(filter(lambda rel: rel.adu == adu.text, relations))

    if candidates:
        relation = candidates[0]

        if relation and relation.classification == RelationClass.ATTACK:
            return ag.SchemeNode(ag.Attack.DEFAULT)

        elif relation and relation.classification == RelationClass.SUPPORT:
            return ag.SchemeNode(ag.Support.DEFAULT)

    return None
