from lib.Graph import Graph
from lib.Node import Node
from lib.Edge import Edge

graph = Graph()

a = Node('A')

b = Node('B')

c = Node('C')

ab = Edge([a, b], 500)

bc = Edge([b, c], 100)

ca = Edge([c, a], 400)

graph.add_edges(ab, bc, ca)

for edge in graph.edges:
    print(edge)

    



