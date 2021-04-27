# ref: https://bit.ly/3nGmgOB

D = dict()


def fib(n):
    """cache version. Similar to @functools.lru_cache
    """
    if n not in D:
        if n <= 1:
            D[n] = n
        else:
            D[n] = fib(n - 1) + fib(n - 2)
    return D[n]


def fib2(n):
    """Storage array
    """
    T = [None] * (n + 1)
    T[0], T[1] = 0, 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]


def fib3(n):
    """Super compact version
    """
    if n <= 1:
        return n

    prev, cur = 0, 1
    for _ in range(n - 1):
        new_cur = prev + cur
        prev, cur = cur, new_cur
    return cur


def test_fib():
    assert fib(10) == 55
    assert fib2(10) == 55
    assert fib3(10) == 55
