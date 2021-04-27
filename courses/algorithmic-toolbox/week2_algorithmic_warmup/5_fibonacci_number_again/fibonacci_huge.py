# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def pisano_period(m):
    "Calculate length of the pisano period"
    prev, cur = 0, 1
    for i in range(m*m):
        prev, cur = cur, (prev + cur) % m
        if (prev, cur) == (0, 1):
            return i+1


def fib(n):
    F = [1, 1]
    for i in range(2, n):
        F.append(F[i-1] + F[i-2])
    return F[n-1]


def get_fibonacci_huge(n, m):
    _n = n % pisano_period(m)
    return fib(_n) % m


# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

def test():
    assert get_fibonacci_huge(239, 1000) == 161
    assert get_fibonacci_huge(2816213588, 239) == 151
