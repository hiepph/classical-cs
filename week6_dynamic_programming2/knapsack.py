import numpy as np

T = dict()


def knapsack(w, v, u):
    if u not in T:
        T[u] = 0

        for i in range(len(w)):
            if w[i] <= u:
                T[u] = max(T[u], knapsack(w, v, u - w[i]) + v[i])
    return T[u]


def iterative_knapsack(w, v, W):
    T = [0] * (W + 1)
    for u in range(1, W + 1):
        for i in range(len(w)):
            if w[i] <= u:
                T[u] = max(T[u], T[u - w[i]] + v[i])
    return T[W]


def test_knapsack():
    assert knapsack(w=[6, 3, 4, 2],
                    v=[30, 14, 16, 9], u=10) == 48  # 30 + 9 + 9
    assert iterative_knapsack(w=[6, 3, 4, 2],
                              v=[30, 14, 16, 9], W=10) == 48  # 30 + 9 + 9


def knapsack_without_repetitions(w, v, W):
    w = [None] + w
    v = [None] + v

    M = np.zeros((len(w), W + 1))
    for i in range(1, len(w)):
        for j in range(1, W + 1):
            M[i, j] = M[i - 1, j]
            if w[i] <= j:
                val = v[i] + M[i - 1, j - w[i]]
                if M[i, j] < val:
                    M[i, j] = val
    return M[-1, -1]


def test_knapsack_without_repetitions():
    assert knapsack_without_repetitions(
        w=[6, 3, 4, 2], v=[30, 14, 16, 9], W=10) == 46
