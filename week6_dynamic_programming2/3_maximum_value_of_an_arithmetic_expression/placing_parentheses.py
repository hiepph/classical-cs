import math
import re
import numpy as np


OPS = "+-*"


def tokenize(s):
    ds = re.split(r"\+|-|\*", s)
    ds = list(map(int, ds))
    ops = re.findall(r"\+|-|\*", s)
    return ds, ops


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def compute_min_max(m, M, i, j, op):
    _min = math.inf
    _max = -math.inf

    for k in range(i, j):
        a = evalt(M[i, k], M[k + 1, j], op[k])
        b = evalt(M[i, k], m[k + 1, j], op[k])
        c = evalt(m[i, k], M[k + 1, j], op[k])
        d = evalt(m[i, k], m[k + 1, j], op[k])
        _min = min(_min, a, b, c, d)
        _max = max(_max, a, b, c, d)
    return _min, _max


def get_maximum_value(dataset):
    d, op = dataset
    n = len(d)
    m = np.zeros((n, n))
    M = np.zeros((n, n))

    for i in range(n):
        m[i, i] = d[i]
        M[i, i] = d[i]

    # diagonal moving
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i, j], M[i, j] = compute_min_max(m, M, i, j, op)
    return M[0, n - 1]


def test():
    assert get_maximum_value(tokenize("1+5")) == 6
    assert get_maximum_value(tokenize("5-8+7*4-8+9")) == 200
