def div3(x):
    return (x // 3, True) if x % 3 == 0 else (-1, False)


def div2(x):
    return (x // 2, True) if x % 2 == 0 else (-1, False)


def minus1(x):
    return (x - 1, True)


T = dict()


def optimal_sequence(n):
    """
    Returns:
    The minimum number of operations
    The intermediate numbers that lead to n
    """
    T = [-1] * (n + 1)
    paths = [-1] * (n + 1)
    for i in reversed(range(1, n + 1)):
        for op in [div3, div2, minus1]:
            v, ok = op(i)
            if ok and (T[v] < 0 or T[i] + 1 < T[v]):
                T[v] = T[i] + 1
                paths[v] = i

    # backtrack
    sequences = []
    cur = 1
    while cur != -1:
        sequences.append(cur)
        cur = paths[cur]
    return T[0], sequences


def test():
    assert optimal_sequence(1) == (0, [1])
    assert optimal_sequence(5) == (3, [1, 3, 4, 5])
    assert optimal_sequence(96234) == (
        14, [1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234])
