from src.depth_traverse import traverse

def is_graph_connected(nodes):
    traverse(nodes[0])

    for node in nodes:
        if not node.visited:
            return False
    return True
