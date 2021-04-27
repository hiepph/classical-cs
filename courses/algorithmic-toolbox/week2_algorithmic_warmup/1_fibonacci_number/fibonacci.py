# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fib(n):
    F = [1, 1]
    for i in range(2, n):
        F.append(F[i-1] + F[i-2])
    return F[n-1]


if __name__ == '__main__':
    n = int(input())
    # print(calc_fib(n))
    print(fib(n))
