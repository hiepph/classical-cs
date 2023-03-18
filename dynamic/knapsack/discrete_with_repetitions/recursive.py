# refer: Dynamic Programming - Alexander S. Kulikov
T = dict()


# W: knapsack weight limit
# w: weights
# v: values, each v[i] == w[i]
def knapsack(W, w, v):
    if W not in T:
        T[W] = 0 # base case

        for i in range(len(w)):
            if w[i] <= W:
                # If we take w[i] out, we retrieve an optimal solution for W - w[i]
                T[W] = max(T[W],
                           knapsack(W - w[i], w, v) + v[i])

    return T[W]


def test():
    assert knapsack(W=10,
                    w=[6, 3, 4, 2],
                    v=[30, 14, 16, 9]) == 48
