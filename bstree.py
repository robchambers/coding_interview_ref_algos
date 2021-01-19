""" Binary search tree. """

from btree import Node


class BSTree(object):
    def __init__(self, root: Node = None):
        self.root = root

    def add_node(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
            return

        current = self.root
        
        while True:
            if current.data < node.data:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
    
    def search(self, target):
        current = self.root
        while current is not None:
            if current.data < target:
                current = current.right
            elif current.data > target:
                current = current.left
            else:
                return current
        
        return None


def test():
    import random

    for l in [1, 2, 5, 10]:
        # ints
        arr = [random.randint(-1000, 1000) for i in range(l)]
        b = BSTree()
        for v in arr:
            b.add_node(v)
        assert b.search(arr[0])
        assert b.search(arr[-1])
        assert not b.search(1.11111)
        print('ok')
        
    # null case
    b = BSTree()
    assert not b.search(1.1111)
    print('ok')

test()

