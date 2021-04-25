def merge(A, l, m, r):
    L = A[l:m + 1]
    R = A[m + 1:r + 1]

    il = ir = 0
    ia = l
    # copy value of subarrays back to A
    while il < len(L) and ir < len(R):
        if L[il] < R[ir]:
            A[ia] = L[il]
            il += 1
        else:
            A[ia] = R[ir]
            ir += 1
        ia += 1

    # copy left values of L/R
    while il < len(L):
        A[ia] = L[il]
        ia += 1
        il += 1
    while ir < len(R):
        A[ia] = R[ir]
        ia += 1
        ir += 1


def MergeSort(A, l, r):
    if r > l:
        m = (l + r) // 2
        MergeSort(A, l, m)
        MergeSort(A, m + 1, r)
        merge(A, l, m, r)


def test():
    A = [6, 3, 4, 2, 9, 7, 8, 5, 2, 6, 1]
    MergeSort(A, 0, len(A) - 1)
    assert A == [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]
