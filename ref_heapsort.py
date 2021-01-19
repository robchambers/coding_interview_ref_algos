""" Quicksort using DNF, good w/ duplicates """

import random
import heapq

def heapsort_in_out_w_key(arr, reverse=False):
    h = []
    for el in arr:
        k = el
        if reverse:
            k = -k
        heapq.heappush(h, (k, el))
    out = []
    while len(h):
        out.append(heapq.heappop(h)[1])
    return out

def test():
    sort_f = heapsort_in_out_w_key
    for l in [0, 1, 2, 5, 10]:
        # ints
        arr = [random.randint(-1000, 1000) for i in range(l)]
        arr2 = sorted(arr)
        arr = sort_f(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

        arr2 = sorted(arr, reverse=True)
        arr = sort_f(arr, reverse=True)
        assert tuple(arr) == tuple(arr2)
        print('ok')

        # floats
        arr = [random.random() for i in range(l)]
        arr2 = sorted(arr)
        arr = sort_f(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

        arr2 = sorted(arr, reverse=True)
        arr = sort_f(arr, reverse=True)
        assert tuple(arr) == tuple(arr2)
        print('ok')

    # dups
    arr = [0, 1, 0, 1, 1, 2]
    arr2 = sorted(arr)
    arr = sort_f(arr)
    assert tuple(arr) == tuple(arr2)
    print('ok')

    arr2 = sorted(arr, reverse=True)
    arr = sort_f(arr, reverse=True)
    assert tuple(arr) == tuple(arr2)
    print('ok')


test()

