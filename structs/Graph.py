class Graph:
    def __init__(self):
        self.edges = []

    def add_edges(self, *edges):
        for edge in edges:
            self.edges.append(edge)