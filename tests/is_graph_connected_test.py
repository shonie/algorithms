import unittest
from src.is_graph_connected import is_graph_connected
from src.structs.Graph import Graph
from src.structs.Node import Node
from src.structs.Edge import Edge

class TestIsGraphConnected(unittest.TestCase):
    def test_returns_false_for_not_connected_graph(self):
        g = Graph()
        g.add_edges(
            Edge([Node('a'), Node('b')], 500),
            Edge([Node('c'), Node('d')], 300)
        )
        self.assertFalse(is_graph_connected(g))

    def test_returns_true_for_connected_graph(self):
        g = Graph()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        g.add_edges(
            Edge([a, b], 500),
            Edge([b, c], 300),
            Edge([c, d], 200)
        )
        self.assertTrue(is_graph_connected(g))

if __name__ == '__main__':
    unittest.main()
