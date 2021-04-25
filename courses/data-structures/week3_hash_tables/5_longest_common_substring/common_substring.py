import sys
import random


def polyhash(s, multiplier, prime):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def make_hash_table(s, k):
    multiplier = 10**9 + 7
    prime = 263

    H = [0] * (len(s) - k + 1)
    # compute rolling hash reversely
    # refer:
    # https://www.coursera.org/learn/data-structures/lecture/nYrc8/optimization-precomputation
    last_sub = s[len(s) - k:]
    H[len(s) - k] = polyhash(last_sub, multiplier, prime)
    # == mutiplier ** k % prime, compute more efficiently
    y = pow(multiplier, k, prime)
    for i in range(len(s) - k - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(s[i]) - y * ord(s[i + k])) % prime
    return H


def check_common_substring(s, t, k):
    # can compute multiple hash table here
    # omit for readability
    Hs = make_hash_table(s, k)
    Ht = make_hash_table(t, k)

    # turn Hs to a dictionary for efficient find
    Ds = dict([h, s_start] for s_start, h in enumerate(Hs))

    # returns:
    # s's start position, t's start position,
    # (boolean) found the commmon substring
    for t_start, sub in enumerate(Ht):
        if sub in Ds:
            s_start = Ds[sub]
            return s_start, t_start, True
    return -1, -1, False


def solve(s, t):
    s_result, t_result = -1, -1

    # binary search to search for the longest length of common substring
    l = 0
    h = min(len(s), len(t))
    while l <= h:
        m = (l + h) // 2
        s_start, t_start, found = check_common_substring(s, t, m)
        if found:
            s_result, t_result = s_start, t_start
            l = m + 1
        else:
            h = m - 1

    # returns:
    # start position of s, start position of t,
    # length of longest common substring
    return s_result, t_result, l - 1


for line in sys.stdin.readlines():
    s, t = line.split()
    s_start, t_start, max_length = solve(s, t)
    print(s_start, t_start, max_length)
