import arggraph as aif
from arg_services.graph.v1 import graph_pb2 as pb


def aif2protobuf(graph_aif: aif.Graph):
    graph_proto = pb.Graph(schema_version=1)

    for node_aif in graph_aif.nodes:
        node_proto = pb.Node()

        if node_aif.category == aif.NodeCategory.I:
            node_proto.atom.text = node_aif.plain_text
        elif node_aif.category == aif.NodeCategory.RA:
            node_proto.scheme.support = pb.SUPPORT_DEFAULT
        elif node_aif.category == aif.NodeCategory.CA:
            node_proto.scheme.attack = pb.ATTACK_DEFAULT
        else:
            raise ValueError(f"Unknown node category: {node_aif.category}")

        graph_proto.nodes[str(node_aif.key)].CopyFrom(node_proto)

    for edge_aif in graph_aif.edges:
        edge_proto = pb.Edge(
            source=str(edge_aif.start.key),
            target=str(edge_aif.end.key),
        )
        graph_proto.edges[str(edge_aif.key)].CopyFrom(edge_proto)

    if graph_aif.major_claim:
        graph_proto.major_claim = str(graph_aif.major_claim.key)

    return graph_proto
