# W: knapsack weight limit
# w: weights
# v: values, each v[i] == w[i]
def knapsack(W, w, v):
    T = [0] * (W + 1)

    for u in range(1, W + 1):
        for i in range(len(w)):
            if w[i] <= u:
                T[u] = max(T[u], T[u - w[i]] + v[i])

    return T[W]


def test():
    assert knapsack(W=10,
                    w=[6, 3, 4, 2],
                    v=[30, 14, 16, 9]) == 48
