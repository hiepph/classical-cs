# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return 0
    # write your code here
    a = sorted(a)  # O(nlogn)
    n = len(a)
    count = 1
    cur = a[0]
    for i in range(1, len(a)):
        if a[i] != cur:
            count = 1
            cur = a[i]
        else:
            count += 1
            if count > n // 2:
                return 1

    return 0


def test_():
    assert get_majority_element([2, 3, 9, 2, 2], 0, 5) == 1
    assert get_majority_element([1, 2, 3, 4], 0, 4) == 0
    assert get_majority_element([1, 2, 3, 1], 0, 4) == 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
