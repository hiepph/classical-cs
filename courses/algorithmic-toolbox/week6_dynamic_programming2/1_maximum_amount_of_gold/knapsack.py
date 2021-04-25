T = dict()


def optimal_weight(W, w):
    if W not in T:
        T[W] = 0

    for i in range(len(w)):
        if w[i] <= W:
            v = w[i]
            remain_w = w.copy()
            remain_w.pop(i)
            T[W] = max(T[W], optimal_weight(W - v, remain_w) + v)
    return T[W]


def test():
    assert optimal_weight(10, [1, 4, 8]) == 9
