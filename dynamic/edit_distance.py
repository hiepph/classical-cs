def edit_distance(A: str, B: str):
    a = len(A)
    b = len(B)

    #
    # create a 2-d cache: with row is A and column is B
    # assume we have an empty char at the start of the string
    #
    cache = [[None for _ in range(b + 1)]
             for _ in range(a + 1)]

    # only deletion operations
    for i in range(a + 1):
        cache[i][0] = i

    # only insertion operations
    for j in range(b + 1):
        cache[0][j] = j

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i - 1] == B[j - 1]:
                # do nothing
                replace = 0
            else:
                replace = 1
            cache[i][j] = min(cache[i - 1][j] + 1,
                              cache[i][j - 1] + 1,
                              cache[i - 1][j - 1] + replace)

    return cache[a][b]


def test():
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("benyam", "ephrem") == 5
    assert edit_distance("zoologicoarchaeologist", "zoogeologist") == 10
