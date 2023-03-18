T = dict()


# time: O(n^2)
def lis(A, i):
    """lis: optimal length of a LIS ending at A[i]"""
    if i not in T:
        T[i] = 1

        for j in range(i):
            if A[j] < A[i]:
                T[i] = max(T[i], lis(A, j) + 1)

    return T[i]


if __name__ == '__main__':
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
    assert max(lis(A, i) for i in range(len(A))) == 5
