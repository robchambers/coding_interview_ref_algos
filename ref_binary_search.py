""" Binary search on sorted array """


def bsearch(arr, t):
    """
    arr: Iterable, sorted.
    t: target.
    return: i or None (index of target)
    """
    if not arr or t is None:
        return None

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)  # or just // 2
        if arr[mid] < t:
            low = mid + 1
        elif arr[mid] > t:
            high = mid - 1
        else:
            return mid

    return None


def bsearch_ins_pos(arr, t, left):
    """ Index where we should insert t in sorted arr. If t exists, then
    we can return the left (left=True) or right (left=False) side of
    the dups range. """

    low = 0
    high = len(arr)  # note search goes 1 higher b/c you might need to insert afterwards

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < t:
            low = mid + 1
        elif arr[mid] > t:
            high = mid
        else:
            if left:
                high = mid
            else:
                low = mid + 1

    return low


def test():
    import random

    for l in [1, 2, 5, 10]:
        arr = [random.random() for i in range(l)]
        arr = sorted(arr)
        i = random.randrange(0, len(arr))
        t = arr[i]

        ret = bsearch(arr, t)

        assert ret == i
        print('ok')

    assert bsearch([], 5) is None
    print('ok')

    assert bsearch([1, 2, 3, 4], 5) is None
    print('ok')

    assert bsearch([1, 2, 3, 4], None) is None
    print('ok')

    arr = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    assert bsearch_ins_pos(arr, 4, True) == 3
    assert bsearch_ins_pos(arr, 4, False) == 7

    arr = [1, 2, 3, 4, 5, 6, 7]
    assert bsearch_ins_pos(arr, 4, True) == 3
    assert bsearch_ins_pos(arr, 4, False) == 4

    arr = [1, 2, 3, 5, 6, 7]
    assert bsearch_ins_pos(arr, 4, True) == 3
    assert bsearch_ins_pos(arr, 4, False) == 3

    arr = [1, 2, 3, 5, 6, 7]
    assert bsearch_ins_pos(arr, 1, True) == 0
    assert bsearch_ins_pos(arr, 1, False) == 1
    assert bsearch_ins_pos(arr, 0, True) == 0
    assert bsearch_ins_pos(arr, 0, False) == 0
    assert bsearch_ins_pos(arr, 7, True) == 5
    assert bsearch_ins_pos(arr, 7, False) == 6
    assert bsearch_ins_pos(arr, 9, True) == 6
    assert bsearch_ins_pos(arr, 9, False) == 6


test()
