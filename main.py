from generate_graph import generate_graph
from depth_traverse import traverse

graph = generate_graph(3)

for edge in graph.edges:
    print(edge)

traverse(graph.edges[0].nodes[0])

