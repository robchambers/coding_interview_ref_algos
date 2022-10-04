""" Merge sort """


def merge(arr, start, mid, end):
    """
    [ x x 0 1 2 3 0 1 2 3 x x ]
          s     m       e
    ->
    [ x x 0 0 1 1 2 2 3 3 x x ]
    """
    result = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    result.extend(arr[i:mid + 1])
    result.extend(arr[j:end + 1])

    arr[start: end + 1] = result


def _merge_sort(arr, start, end):
    if start >= end:
        return

    mid = start + (end - start) // 2

    _merge_sort(arr, start, mid)
    _merge_sort(arr, mid + 1, end)

    merge(arr, start, mid, end)


def merge_sort(arr):
    _merge_sort(arr, 0, len(arr) - 1)


def test():
    import random

    for l in [0, 1, 2, 5, 10]:
        # ints
        arr = [random.randint(-1000, 1000) for i in range(l)]
        arr2 = sorted(arr)
        merge_sort(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

        # floats
        arr = [random.random() for i in range(l)]
        arr2 = sorted(arr)
        merge_sort(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

    # dups
    arr = [0, 1, 0, 1, 1, 2]
    arr2 = sorted(arr)
    merge_sort(arr)
    assert tuple(arr) == tuple(arr2)
    print('ok')


test()
