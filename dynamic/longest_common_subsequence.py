#
# ref: https://youtu.be/ASoaQq66foQ
# time: O(mn)
# space: O(mn)
#
def longest_common_subsequence(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    # dynamic table with size (m + 1) x (n + 1)
    # assume we have an empty char at the start of each string
    cache = [[0 for _ in range(m + 2)]
             for _ in range(n + 2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # minus one char from both string
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                # get max of 2 subproblems:
                # + minus one char from s1
                # + minus one char from s2
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[m][n]


def test():
    assert(longest_common_subsequence("aab", "azb") == 2)
    assert(longest_common_subsequence("GXTXAYB", "AGGTAB") == 4)
