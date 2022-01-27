def knapsack(values, weights, W) -> int:
    """
    Args:
        W: knapsack capacity

    Returns:
        Maximum value within the capacity
    """
    n = len(values)
    cache = [[0 for _ in range(W + 1)]
             for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] > j:
                cache[i][j] = cache[i - 1][j]
            else:
                cache[i][j] = max(
                    cache[i - 1][j],
                    cache[i - 1][j - weights[i - 1]] + values[i - 1])

    return cache[-1][-1]


def test():
    assert(knapsack([60, 50, 70, 30], [5, 3, 4, 2], 5) == 80)
