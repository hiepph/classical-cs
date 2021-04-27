T = dict()


def lis(A):
    T = [None] * len(A)

    for i in range(len(A)):
        T[i] = 1
        for j in range(i):
            if A[j] < A[i] and T[i] < T[j] + 1:
                T[i] = T[j] + 1

    return max(T[i] for i in range(len(A)))


def cons_lis(A):
    """Reconstruct the optimal solution
    """
    T = [None] * len(A)
    prev = [None] * len(A)

    for i in range(len(A)):
        T[i] = 1
        prev[i] = -1
        for j in range(i):
            if A[j] < A[i] and T[i] < T[j] + 1:
                T[i] = T[j] + 1
                prev[i] = j

    # unwinding the solution
    last = 0
    for i in range(1, len(A)):
        if T[i] > T[last]:
            last = i

    paths = []
    cur = last
    while cur >= 0:
        paths.append(A[cur])
        cur = prev[cur]
    paths.reverse()
    return paths


D = dict()


def lis2(A, last_index):
    """Recursion optimization.
    It remains to add memoization through `last_index`"""
    ##
    if last_index in D:
        return D[last_index]
    ##

    if last_index == -1:
        last_element = float("-inf")
    else:
        last_element = A[last_index]
    result = 0

    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, 1 + lis2(A, i))

    ##
    if last_index not in D:
        D[last_index] = result
    ##

    return result


def test_lis():
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
    assert lis(A) == 5
    assert cons_lis(A) == [2, 3, 4, 6, 9]

    assert lis2(A, last_index=-1) == 5
