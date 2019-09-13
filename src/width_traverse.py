from collections import deque

def traverse(node, visitor):
    visited = set([node])
    visitor(node)
    queue = deque([node])
    while queue:
        n = queue.popleft()
        for edge in n.edges:
            to_node = edge.nodes[1]
            if not to_node in visited:
                visited.add(to_node)
                visitor(to_node)
                queue.append(to_node)
