# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def pisano(m):
    "Return the pisano sequence"
    seq = [0, 1]
    prev, cur = 0, 1
    for i in range(m*m):
        prev, cur = cur, (prev + cur) % m
        seq.append(cur)
        if (prev, cur) == (0, 1):
            return seq[:-2]

def fibonacci_sum_squares(n):
    # get last digits aka modulo 10
    last_digits = pisano(10)
    # get 'last digits' of F_n, F_(n+1)
    cur, next = last_digits[n % len(last_digits)], last_digits[(n+1) % len(last_digits)]
    # sum = area = F_n * F_(n+1)
    return (cur * next) % 10

def test():
    assert fibonacci_sum_squares(7) == 3
    assert fibonacci_sum_squares(73) == 1
    assert fibonacci_sum_squares(1234567890) == 0
