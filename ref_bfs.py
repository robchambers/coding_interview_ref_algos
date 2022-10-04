""" Breadth first search of a graph. Returns True if target exists in the graph. """

from graph import *
from collections import deque


# deque:
# .popleft(), .appendleft(x),  ---   , .append(x), .pop()

def bfs_visit(node, target):
    q = deque()
    q.append(node)
    node.state = States.VISITING

    while len(q):
        cur = q.popleft()

        # visit
        if cur.data == target:
            return True

        for n in cur.neighbors:
            if n.state == States.UNVISITED:
                q.append(n)
                n.state = States.VISITING

        cur.state = States.VISITED

    return False


def bfs(graph, target):
    for node in graph.nodes:
        node.state = States.UNVISITED

    for node in graph.nodes:
        if node.state == States.UNVISITED:
            if bfs_visit(node, target):
                return True

    return False


def test():
    import random

    for l in [1, 2, 5, 10]:
        g = Graph(
            nodes=[Node(data=random.random()) for i in range(l + 1)]
        )
        for n in g.nodes:
            n.neighbors = random.sample(g.nodes, random.randrange(0, len(g.nodes)))

        ret = bfs(g, random.choice(g.nodes).data)
        assert ret
        print('ok')

        ret = bfs(g, 1.2342)
        assert not ret
        print('ok')

    g = Graph()
    ret = bfs(g, 1)
    assert not ret
    print('ok')


test()
