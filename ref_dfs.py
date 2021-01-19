""" Depth first search of a graph. Returns True if target exists in the graph. """

from graph import *


def dfs_visit(node, target):
    node.state = States.VISITING

    if node.data == target:
        return True
    
    for n in node.neighbors:
        if n.state is States.UNVISITED:
            if dfs_visit(n, target):
                return True
    
    node.state = States.VISITED

    return False


def dfs(graph, target):
    for node in graph.nodes:
        node.state = States.UNVISITED

    for node in graph.nodes:
        if node.state is States.UNVISITED:
            if dfs_visit(node, target):
                return True
    
    return False

def test():

    import random


    for l in [1, 2, 5, 10]:
        g = Graph(
            nodes = [Node(data=random.random()) for i in range(l+1)]
        )
        for n in g.nodes:
            n.neighbors = random.sample(g.nodes, random.randrange(0, len(g.nodes)))
        
        ret = dfs(g, random.choice(g.nodes).data)
        assert ret
        print('ok')

        ret = dfs(g, 1.2342)
        assert not ret
        print('ok')

    g = Graph()
    ret = dfs(g, 1)
    assert not ret
    print('ok')


test()

