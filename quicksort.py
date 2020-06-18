import random


def QuickSort(A, l, r):
    if l >= r:
        return

    # randomize
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]

    m = Partition(A, l, r)
    QuickSort(A, l, m - 1)
    QuickSort(A, m + 1, r)


def Partition(A, l, r):
    p = A[l]
    j = l
    for i in range(l + 1, r + 1):
        if A[i] <= p:
            j = j + 1
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def test():
    A = [6, 3, 4, 2, 9, 7, 8, 5, 2, 6, 1]
    QuickSort(A, 0, len(A) - 1)
    assert A == [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]
