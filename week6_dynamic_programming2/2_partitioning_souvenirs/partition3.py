import numpy as np


def partition(W, items):
    count = 0

    n = len(items)
    M = np.zeros((n + 1, W + 1))

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            M[i, w] = M[i - 1, w]
            if items[i - 1] <= w:
                temp = items[i - 1] + M[i - 1, w - items[i - 1]]
                if M[i, w] < temp:
                    M[i, w] = temp
            if M[i, w] == W:
                count += 1

    return 1 if count >= 3 else 0


def partition3(A):
    """
    Resembles with discrete Knapsack problem without repetition.
    Count the number of tracks which makes to sum(A) / 3
    """
    return partition(sum(A) // 3, A)


def test():
    assert partition3([3, 3, 3, 3]) == 0
    assert partition3([40]) == 0
    assert partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == 1
    assert partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1
