import unittest
from src.depth_traverse import traverse
from src.generate_graph import generate_graph

class TestDepthTraverse(unittest.TestCase):
    def test_visits_all_nodes(self):
        g = generate_graph(5)
        nodes = g.get_nodes()
        visited_count = 0
        def visitor(node):
            nonlocal visited_count
            visited_count += 1
        traverse(nodes[0], visitor)
        self.assertEqual(visited_count, len(nodes))

    @unittest.skip('The graph is being generated randomly, figure out how to test its traversing flow')
    def test_traverses_deep_nodes_before_shallow_nodes(self):
        g = generate_graph(3, False)
        nodes = g.get_nodes()
        last_visited_node = None
        def visitor(node):
            nonlocal last_visited_node
            last_visited_node = node
        traverse(nodes[0], visitor)
        self.assertEqual(last_visited_node, nodes[1])

if __name__ == '__main__':
    unittest.main()
