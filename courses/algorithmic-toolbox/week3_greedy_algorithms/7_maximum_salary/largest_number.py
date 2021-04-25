# Uses python3

import sys
import functools


def cmp(a, b):
    return int(f"{a}{b}") - int(f"{b}{a}")


def largest_number(a):
    a = sorted(a, key=functools.cmp_to_key(cmp))
    a = reversed(a)
    return ''.join(a)


def test():
    assert largest_number(["21", "2"]) == "221"
    assert largest_number(["23", "39", "92"]) == "923923"


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
