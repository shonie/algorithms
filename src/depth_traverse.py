def traverse(node, visitor):
    visited = set([node])
    visitor(node)
    stack = []
    stack.append(node)
    while stack:
        n = stack.pop()
        for edge in n.edges:
            to_node = edge.nodes[1]
            if not to_node in visited:
                visited.add(to_node)
                visitor(to_node)
                stack.append(to_node)
