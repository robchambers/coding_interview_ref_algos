""" Depth first search of a graph, but done iteratively. Returns True if target exists in the graph. """

from graph import *


def dfs(graph, target):
    for node in graph.nodes:
        node.state = States.UNVISITED

    stack = graph.nodes

    while len(stack):
        node = stack.pop()

        if node.state == States.UNVISITED:
            node.state = States.VISITING

            if node.data == target:
                return True

            for n in node.neighbors:
                if n.state == States.UNVISITED:
                    stack.append(n)

            node.state = States.VISITED

    return False


def test():
    import random

    for l in [1, 2, 5, 10]:
        g = Graph(
            nodes=[Node(data=random.random()) for i in range(l + 1)]
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
