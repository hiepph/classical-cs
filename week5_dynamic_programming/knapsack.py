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
