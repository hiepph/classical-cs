def edit_distance(A, B):
    A = "^" + A
    B = "^" + B

    D = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            row.append(0)
        D.append(row)

    for i in range(1, len(A)):
        D[i][0] = i
    for j in range(1, len(B)):
        D[0][j] = j
    for j in range(1, len(B)):
        for i in range(1, len(A)):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if A[i] == B[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[len(A) - 1][len(B) - 1]


def test_edit_distance():
    assert(edit_distance("editing", "edit")) == 3
    assert(edit_distance("editing", "distance")) == 5
