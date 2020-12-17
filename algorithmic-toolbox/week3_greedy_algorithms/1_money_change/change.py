# Uses python3
import sys

values = [1, 5, 10]

def get_change(m):
    n = 0
    while m > 0:
        # get the max available value (under m)
        available_values = list(filter(lambda x: x <= m, values))
        m -= max(available_values)
        n += 1

    return n

def test_get_change():
    assert get_change(2) == 2
    assert get_change(28) == 6


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
