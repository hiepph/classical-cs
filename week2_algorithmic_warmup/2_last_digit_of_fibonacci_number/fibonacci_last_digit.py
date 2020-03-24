# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    F = [1, 1]
    for i in range(2, n):
        F.append((F[i-1] + F[i-2]) % 10)
    return F[n-1]



if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
