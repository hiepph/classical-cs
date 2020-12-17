# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    F = [0, 1]
    # keep only last digits
    for i in range(2, to+1):
        F.append((F[i-1] + F[i-2]) % 10)
    sum = 0
    for i in range(from_, to+1):
        print(F[i])
        sum = (sum + F[i]) % 10
    return sum



def test():
    assert fibonacci_partial_sum(3, 7)  == 1
    assert fibonacci_partial_sum(10, 10)  == 5
    assert fibonacci_partial_sum(10, 200)  == 2
