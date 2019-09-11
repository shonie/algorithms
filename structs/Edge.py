class Edge:
    def __init__(self, nodes, cost):
        self.nodes = nodes
        self.cost = cost

    def __str__(self):
        from_node = self.nodes[0]
        to_node = self.nodes[1]
        return f'From node {from_node.name} to {to_node.name}, cost - {self.cost}' 
