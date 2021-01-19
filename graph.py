import enum

class States(enum.Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

class Node(object):
    def __init__(self, neighbors=None, data=None, state=States.UNVISITED):
        if neighbors is None:
            neighbors = []
        self.neighbors = neighbors
        self.data = data
        self.state = state
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Graph(object):
    def __init__(self, nodes = None):
        if nodes is None:
            nodes = []
        self.nodes = nodes
    
    def add_node(self, node):
        self.nodes.append(node)