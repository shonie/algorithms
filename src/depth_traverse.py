def traverse(node):
    node.visited = True
    stack = []
    stack.append(node)
    while stack:
        n = stack.pop()
        for edge in n.edges:
            to_node = edge.nodes[1]
            if not to_node.visited:
                to_node.visited = True
                stack.append(to_node)
