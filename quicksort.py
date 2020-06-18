import random


def QuickSort(A, l, r):
    if l >= r:
        return

    # randomize
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]

    m1, m2 = Partition3(A, l, r)
    QuickSort(A, l, m1 - 1)
    QuickSort(A, m2 + 1, r)


def Partition3(A, l, r):
    p = A[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if A[i] < p:
            A[m1], A[i] = A[i], A[m1]
            m1 += 1
            i += 1
        elif A[i] > p:
            A[m2], A[i] = A[i], A[m2]
            m2 -= 1
        else:
            i += 1

    return m1, m2


def test():
    A = [6, 3, 4, 2, 9, 7, 8, 5, 2, 6, 1]
    QuickSort(A, 0, len(A) - 1)
    assert A == [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]
