""" Quickselect using single-placement partitioning """

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def spp(arr, start, end, ipivot) -> (int, int):
    swap(arr, start, ipivot)
    lo = start # last el in left partition

    for i in range(start + 1, end + 1):
        if arr[i] <= arr[start]:
            swap(arr, lo + 1, i)
            lo += 1
    
    swap(arr, start, lo)

    return lo

def _quickselect(arr, start, end, k):
    ipivot = random.randrange(start, end + 1)
    ipivot = spp(arr, start, end, ipivot)

    if ipivot > k:
        return _quickselect(arr, start, ipivot - 1, k)
    elif ipivot < k:
        return _quickselect(arr, ipivot + 1, end, k)
    else:
        return arr[k]

def quickselect(arr, k):
    assert k < len(arr)
    return _quickselect(arr, 0, len(arr) - 1, k)


def test():
    for l in [1, 2, 5, 10]:
        # ints
        arr = [random.randint(-1000, 1000) for i in range(l)]
        arr2 = sorted(arr)
        k = random.randrange(0, l)
        ret1 = arr2[k]
        ret2 = quickselect(arr, k)
        assert ret1 == ret2
        print('ok')

        # floats
        arr = [random.random() for i in range(l)]
        arr2 = sorted(arr)
        k = random.randrange(0, l)
        ret1 = arr2[k]
        ret2 = quickselect(arr, k)
        assert ret1 == ret2
        print('ok')

    # dups
    arr = [0, 1, 0, 1, 1, 2]
    arr2 = sorted(arr)
    for k in range(0, len(arr)):
        ret1 = arr2[k]
        ret2 = quickselect(arr, k)
        assert ret1 == ret2
    print('ok')


test()

