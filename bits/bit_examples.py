# refer:
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
def count_one(n):
    count = 0
    while n:
        n = n & (n - 1)  # remove last bit
        count += 1
    return count


def test():
    x = int("10110", 2)
    assert count_one(x) == 3
