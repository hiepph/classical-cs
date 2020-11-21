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
    for i in reversed(range(1, n + 1)):
        for op in [div3, div2, minus1]:
            v, ok = op(i)
            if ok and (T[v] < 0 or T[v] > T[i] + 1):
                T[v] = T[i] + 1
    return T[0]


def test():
    assert optimal_sequence(1) == (0, [1])[0]
    assert optimal_sequence(5) == (3, [1, 2, 4, 5])[0]
    assert optimal_sequence(96234) == (14, [1, 2, 4, 5])[0]
