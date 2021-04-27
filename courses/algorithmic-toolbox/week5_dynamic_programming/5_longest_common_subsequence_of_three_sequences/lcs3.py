import numpy as np


def lcs3(a, b, c):
    a = [None] + a
    b = [None] + b
    c = [None] + c

    # build a 3-d array
    M = np.zeros((len(a), len(b), len(c)))
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            for k in range(1, len(c)):
                if a[i] == b[j] == c[k]:
                    M[i][j][k] = M[i - 1][j - 1][k - 1] + 1
                else:
                    M[i][j][k] = max(M[i - 1][j][k], M[i]
                                     [j - 1][k], M[i][j][k - 1])
    return int(M[-1][-1][-1])


def test():
    assert lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5]) == 2
    assert lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7],
                [6, 8, 3, 1, 4, 7]) == 3
