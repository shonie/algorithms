from math import floor
from structs.Graph import Graph
from structs.Node import Node
from structs.Edge import Edge
from random import randint


def generate_graph(number_of_nodes):
    graph = Graph()

    nodes = [Node(i) for i in range(0, number_of_nodes)]

    connected_nodes = set()

    while (len(connected_nodes) < len(nodes)):
        for node in nodes:
            to_node = nodes[randint(0, len(nodes) - 1)]
            if to_node != node:
                edge = Edge([node, to_node], randint(0, 100))
                if not edge in node.edges and not edge in to_node.edges:
                    node.edges.add(edge)
                    to_node.edges.add(edge)
                    graph.add_edges(edge)
                    connected_nodes.add(node)
                    connected_nodes.add(to_node)

    return graph