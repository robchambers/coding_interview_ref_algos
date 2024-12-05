"""  Backtracking ref impls

see https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
"""

import random


def subsets(arr):
    def backtrack(tmp, start, end):
        ret.append(tmp[:])

        for i in range(start, end):
            tmp.append(arr[i])
            backtrack(tmp, i + 1, end)
            tmp.pop()

    ret = []
    backtrack([], 0, len(arr))
    return ret


def permutations(arr, n=None):
    if n is None:
        n = len(arr)

    def backtrack(start, end):
        if start == n:
            ret.append(arr[:n])
            return

        for i in range(start, end):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1, end)
            arr[start], arr[i] = arr[i], arr[start]

    ret = []
    backtrack(0, len(arr))
    return ret


def combinations(arr, n):
    def backtrack(tmp, start, end):
        if len(tmp) == n:
            ret.append(tmp[:])
            return

        for i in range(start, end):
            tmp.append(arr[i])
            backtrack(tmp, i + 1, end)
            tmp.pop()

    ret = []
    backtrack([], 0, len(arr))
    return ret


def test():
    import itertools

    for l in [0, 1, 2, 5]:
        arr = [random.randint(-5, 5) for i in range(l)]
        for n in [0, 1, len(arr)]:
            if n > len(arr):
                continue
            ret = itertools.combinations(arr, 2)
            ret = tuple(sorted([tuple(sorted(r)) for r in ret]))
            ret2 = combinations(arr, 2)
            ret2 = tuple(sorted([tuple(sorted(r)) for r in ret2]))
            # print(len(ret))
            # print(len(ret2))
            # print(ret)
            # print(ret2)
            assert ret == ret2
            print('ok')

            ret = itertools.permutations(arr, n)
            ret = tuple(sorted([tuple(sorted(r)) for r in ret]))
            ret2 = permutations(arr, n)
            ret2 = tuple(sorted([tuple(sorted(r)) for r in ret2]))
            # print(len(ret))
            # print(len(ret2))
            # print(ret)
            # print(ret2)
            assert ret == ret2
            print('ok')

        ret = []
        for i in range(len(arr) + 1):
            ret += itertools.combinations(arr, i)
        ret = tuple(sorted([tuple(sorted(r)) for r in ret]))
        ret2 = subsets(arr)
        ret2 = tuple(sorted([tuple(sorted(r)) for r in ret2]))
        # print(len(ret))
        # print(len(ret2))
        # print(ret)
        # print(ret2)
        assert ret == ret2
        print('ok')


test()
