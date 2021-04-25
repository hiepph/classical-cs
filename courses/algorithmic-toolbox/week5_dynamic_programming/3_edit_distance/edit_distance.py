def edit_distance(s, t):
    s = "^" + s
    t = "^" + t

    D = []
    for i in range(len(s)):
        row = []
        for j in range(len(t)):
            row.append(0)
        D.append(row)

    for i in range(1, len(s)):
        D[i][0] = i
    for j in range(1, len(t)):
        D[0][j] = j
    for j in range(1, len(t)):
        for i in range(1, len(s)):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if s[i] == t[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[len(s) - 1][len(t) - 1]


def test_edit_distance():
    assert(edit_distance("ab", "ab")) == 0
    assert(edit_distance("short", "ports")) == 3
    assert(edit_distance("editing", "edit")) == 3
    assert(edit_distance("editing", "distance")) == 5
