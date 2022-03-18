def longest_common_substring(s1: str, s2: str) -> str:
    m = len(s1)
    n = len(s2)

    # check for discontinuous characters
    max_length = 0
    ending_index = m

    cache = [[0 for _ in range(n + 2)] for _ in range(m + 2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            if cache[i][j] > max_length:
                max_length = cache[i][j]
                ending_index = i

    return s1[ending_index - max_length : ending_index]


def test():
    assert longest_common_substring("libgen", "genius") == "gen"

    assert longest_common_substring("carpenter", "sharpener") == "arpen"

    # different from longest common subsequence
    # bc...d != bcd
    assert longest_common_substring("abcad", "bcd") == "bc"
