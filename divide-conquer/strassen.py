#
# Using Strassen's algorithm for calculating
#  the multiplication of 2 matrices.
# Time: O(n^lg7)
#
# refer: https://www.youtube.com/watch?v=OSelhO6Qnlc
#
import numpy as np


def split(matrix):
    n = len(matrix)
    return matrix[:n//2, :n//2], \
        matrix[:n//2, n//2:], \
        matrix[n//2:, :n//2], \
        matrix[n//2:, n//2:]


def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.ones([n, p]) * 0

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C

def strassen(A, B):
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)

    # ae = strassen(a, e)
    # bg = strassen(b, g)
    # af = strassen(a, f)
    # bh = strassen(b, h)
    # ce = strassen(c, e)
    # dg = strassen(d, g)
    # cf = strassen(c, f)
    # dh = strassen(d, h)
    # C11 = ae + bg
    # C12 = af + bh
    # C21 = ce + dg
    # C22 = cf + dh

    p1 = strassen(a+d, e+h)
    p2 = strassen(d, g-e)
    p3 = strassen(a+b, h)
    p4 = strassen(b-d, g+h)
    p5 = strassen(a, f-h)
    p6 = strassen(c+d, e)
    p7 = strassen(a-c, e+f)
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7

    C = np.vstack(((np.hstack((C11, C12))), np.hstack((C21, C22))))
    return C


def main():
    n = 6
    A = np.tile([1, 2, 3, 4], (4, 1))
    B = np.tile([5, 6, 7, 8], (4, 1))
    C = strassen(A, B)
    assert (C == np.tile([50, 60, 70, 80], (4, 1))).all()


main()
