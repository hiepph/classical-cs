def lcs2(a, b):
    a = [None] + a
    b = [None] + b

    M = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            row.append(0)
        M.append(row)

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                M[i][j] = M[i][j - 1] + 1
            else:
                M[i][j] = max(M[i][j - 1], M[i - 1][j])

    return M[len(a) - 1][len(b) - 1]


def test():
    assert(lcs2([2, 7, 5], [2, 5])) == 2
    assert(lcs2([7], [1, 2, 3, 4])) == 0
    assert(lcs2([2, 7, 8, 3], [5, 2, 8, 7])) == 2
