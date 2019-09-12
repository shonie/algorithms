import random
from src.structs.Graph import Graph
from src.structs.Node import Node
from src.structs.Edge import Edge

def create_and_append_edges(graph, a, b):
    edge = Edge([a, b], random.randint(0, 100))
    back_edge = Edge([b, a], random.randint(0, 100))
    a.edges.append(edge)
    b.edges.append(back_edge)
    graph.add_edges(edge)
    graph.add_edges(back_edge)

def generate_graph(number_of_nodes):
    graph = Graph()
    not_connected_nodes = [Node(i) for i in range(0, number_of_nodes)]
    a = not_connected_nodes.pop()
    b = not_connected_nodes.pop()
    connected_nodes = [a, b]
    create_and_append_edges(graph, *connected_nodes)

    while not_connected_nodes:
        node = random.choice(connected_nodes)
        to_node = not_connected_nodes.pop()
        create_and_append_edges(graph, node, to_node)
        connected_nodes.append(to_node)

    return graph
