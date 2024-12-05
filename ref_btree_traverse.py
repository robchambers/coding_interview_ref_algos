""" Traverse binary tree in pre, in-, and post-order. """

from btree import *


def visit(n, **kwargs):
    print(n.data)
    kwargs["ret"].append(n.data)


def pre_o(n, **kwargs):
    if not n:
        return

    visit(n, **kwargs)
    pre_o(n.left, **kwargs)
    pre_o(n.right, **kwargs)


def in_o(n, **kwargs):
    if not n:
        return

    in_o(n.left, **kwargs)
    visit(n, **kwargs)
    in_o(n.right, **kwargs)


def post_o(n, **kwargs):
    if not n:
        return

    post_o(n.left, **kwargs)
    post_o(n.right, **kwargs)
    visit(n, **kwargs)


def pre_o_iter(n, **kwargs):
    stack = []
    stack.append(n)

    while len(stack):
        n = stack.pop()
        if n:
            visit(n, **kwargs)
            stack.append(n.right)
            stack.append(n.left)


def in_o_iter(n, **kwargs):
    stack = []
    while stack or n:
        while n:
            stack.append(n)
            n = n.left
        n = stack.pop()
        visit(n, **kwargs)
        n = n.right


# def post_o_iter(n, **kwargs):
#     stack = []
#     while stack or n:
#         while n:
#             if n.right:
#                 stack.append(n.right)
#             stack.append(n)
#             n = n.left

#         n = stack.pop()

#         if len(stack) and stack[-1] == n.right: # swap when we get back to a root
#             stack.pop()
#             stack.append(n)
#             n = n.right
#         else:
#             visit(n, **kwargs)
#             n = None


def test():
    """
        1
    2        3
          4     5
        6          7
    """
    b = Node(1, Node(2), Node(3, Node(4, Node(6), None), Node(5, None, Node(7))))
    ret = []
    pre_o(b, ret=ret)
    print(ret)
    assert tuple(ret) == (1, 2, 3, 4, 6, 5, 7)

    ret = []
    pre_o_iter(b, ret=ret)
    print(ret)
    assert tuple(ret) == (1, 2, 3, 4, 6, 5, 7)

    ret = []
    in_o(b, ret=ret)
    print(ret)
    assert tuple(ret) == (2, 1, 6, 4, 3, 5, 7)

    ret = []
    in_o_iter(b, ret=ret)
    print(ret)
    assert tuple(ret) == (2, 1, 6, 4, 3, 5, 7)

    ret = []
    post_o(b, ret=ret)
    print(ret)
    assert tuple(ret) == (2, 6, 4, 7, 5, 3, 1)

    ret = []
    post_o_iter(b, ret=ret)
    print(ret)
    assert tuple(ret) == (2, 6, 4, 7, 5, 3, 1)


test()
