def traverse(node):
    visited = set()
    visited.add(node)
    stack = []
    stack.append(node)
    while stack:
        n = stack.pop()
        print(f'Node {n.name} has {len(n.edges)} edges')
        for edge in n.edges:
            to_node = edge.nodes[1]
            # print('Edge: ', edge)
            # print('To node: ', to_node.name)
            # print('Is visited', to_node in visited)
            # print('------')
            if not to_node in visited:
                visited.add(to_node)
                stack.append(to_node)

    for v in visited:
        print('Node name', v.name)
        print('Node edges')
        for edge in v.edges:
            print(edge.cost)