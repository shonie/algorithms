class Graph:
    def __init__(self):
        self.edges = []

    def add_edges(self, *edges):
        for edge in edges:
            self.edges.append(edge)

    def get_nodes(self):
        nodes = set()
        for edge in self.edges:
            nodes.add(edge.nodes[0])
            nodes.add(edge.nodes[1])
        return [n for n in nodes]
            