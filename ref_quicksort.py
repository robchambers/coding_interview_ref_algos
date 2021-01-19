""" Quicksort using DNF, good w/ duplicates """

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dnf(arr, start, end, ipivot) -> (int, int):
    """ 
    Returns the border points (l, h) outside the middle section
    [0,0,0,1,1,1,2,2,2]
     s   l       h   e
    """

    pivot = arr[ipivot]
    
    low = start - 1 # last el in left partition
    mid = start - 1 # last el in mid partitioni
    high = end + 1  # first el in right parition

    while mid + 1 < high:
        if arr[mid + 1] > pivot:
            swap(arr, mid + 1, high - 1)
            high -= 1
        elif arr[mid + 1] == pivot:
            # swap(mid + 1, mid + 1)# noop
            mid += 1
        else: # arr[mid + 1] < pivot:
            swap(arr, mid + 1, low + 1)
            low += 1
            mid += 1
        
    return (low, high)

def _quicksort(arr, start, end):
    if start >= end:
        return
    ipivot = random.randrange(start, end + 1)
    low, high = dnf(arr, start, end, ipivot)
    _quicksort(arr, start, low)
    _quicksort(arr, high, end)


def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)


def test():
    for l in [0, 1, 2, 5, 10]:
        # ints
        arr = [random.randint(-1000, 1000) for i in range(l)]
        arr2 = sorted(arr)
        quicksort(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

        # floats
        arr = [random.random() for i in range(l)]
        arr2 = sorted(arr)
        quicksort(arr)
        assert tuple(arr) == tuple(arr2)
        print('ok')

    # dups
    arr = [0, 1, 0, 1, 1, 2]
    arr2 = sorted(arr)
    quicksort(arr)
    assert tuple(arr) == tuple(arr2)
    print('ok')


test()

