from typing import List


def bisect_left(arr: List[int], x, low: int = 0, high: int = None) -> int:
    """Return the left most index where to insert item x in list arr, assuming arr is sorted.

    The reutrn value i is such that all e in a[:i] have e < x,
    and all e in a[i:] have e >= x.
    """
    if high is None:
        high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low


def bisect_right(arr: List[int], x, low: int = 0, high: int = None) -> int:
    """Return the right most index where to insert item x in list arr, assuming arr is sorted.

    The reutrn value i is such that all e in a[:i] have e < x,
    and all e in a[i:] have e >= x.
    """
    if high is None:
        high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1
    return low


def test_left():
    assert bisect_left([4, -1, 0, 0, 2, 5], 1) == 4
    assert bisect_left([4, -1, 0, 0, 2, 5], 0) == 2


def test_right():
    assert bisect_right([4, -1, 0, 0, 2, 5], 6) == 6
    assert bisect_right([4, -1, 0, 0, 2, 5], 0) == 4
