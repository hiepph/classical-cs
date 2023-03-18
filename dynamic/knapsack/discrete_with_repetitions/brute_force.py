# Populate a list of used items one by one
def knapsack(W, w, v, items):
    weight = sum(w[i] for i in items)
    value = sum(v[i] for i in items)

    for i in range(len(w)):
        if weight + w[i] <= W:
            # Notice that to optimise,
            # the only important thing for extending the current set of items is the weight of this set
            # One then can replace `items` by their weight in the list of parameters.
            # See `recursive.py`
            value = max(value,
                        knapsack(W, w, v, items + [i]))

    return value


def test():
    assert knapsack(W=10,
                    w=[6, 3, 4, 2],
                    v=[30, 14, 16, 9],
                    items=[]) == 48
