# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    values_per_weight = map(lambda t: t[0] / t[1], zip(values, weights))
    values_per_weight = sorted(values_per_weight)
    while capacity > 0:
        capacity -= 1
        value += values_per_weight[-1]
        weights[-1] -= 1
        if weights[-1] == 0:
            values_per_weight.pop()
            weights.pop()

    return value


def close_enough(a, b):
    return abs(a-b) <= 0.01


def test():
    assert get_optimal_value(50, [20, 50, 30], [60, 100, 120]) == 180
    assert close_enough(get_optimal_value(10, [30], [500]), 166.67)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    breakpoint()
    print("{:.10f}".format(opt_value))
