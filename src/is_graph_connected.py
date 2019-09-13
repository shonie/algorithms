from src.depth_traverse import traverse

def is_graph_connected(graph):
    counter = 0
    def visitor(node):
        nonlocal counter
        counter += 1
    traverse(graph.edges[0].nodes[0], visitor)
    return counter == len(graph.get_nodes())
