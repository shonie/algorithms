import unittest
from src.generate_graph import generate_graph
from src.is_graph_connected import is_graph_connected

class TestGenerateGraph(unittest.TestCase):
    def test_creates_graph_of_two_nodes(self):
        g = generate_graph(2)
        self.assertEqual(len(g.edges), 2)

    def test_creates_connected_graph(self):
        g = generate_graph(5)
        self.assertTrue(is_graph_connected(g))


if __name__ == '__main__':
    unittest.main()
