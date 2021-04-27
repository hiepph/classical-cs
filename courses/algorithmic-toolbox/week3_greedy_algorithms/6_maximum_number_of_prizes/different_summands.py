# Uses python3
import sys


def optimal_summands(n):
    if n == 2:
        return [2]

    summands = []
    i = 0
    remain = n
    while remain > 0:
        i += 1
        possible_remain = remain - i
        if possible_remain in summands or possible_remain == i:
            continue
        else:
            remain = possible_remain
            summands.append(i)
    return summands


def test():
    assert optimal_summands(2) == [2]
    assert optimal_summands(6) == [1, 2, 3]
    assert optimal_summands(8) == [1, 2, 5]
    assert optimal_summands(27) == [1, 2, 3, 4, 5, 12]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
