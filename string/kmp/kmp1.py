def kmp(s, pattern):
    res = []

    table = build_table(pattern)
    print(table)

    i_s = i_p = 0
    while i_s < len(s):
        if pattern[i_p] == s[i_s]:
            i_s += 1
            i_p += 1

        if i_p == len(pattern):
            # found pattern, backward one index to matched prefix
            res.append(i_s - i_p)
            i_p = table[i_p - 1]
            continue

        if pattern[i_p] != s[i_s]:
            # mismatch,
            # if index of the pattern is different than zero,
            # backward one index to matched prefix
            # else, increase the index of string to continue searching
            if i_p != 0:
                i_p = table[i_p - 1]
            else:
                i_s += 1

    return res


def build_table(pattern):
    # table[i]: where to start matching in pattern
    # after a mismatch at i+1
    # aka length of longest suffix which also a prefix
    # of the pattern from index 0 -> i
    table = [0] * len(pattern)

    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            j += 1
        else:
            if i == 0:
                table[j] = 0
                j += 1
            else:
                # tricky, back to previous matched prefix
                i = table[i - 1]

    return table


def test():
    assert kmp("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp("oops, too many oops", "oops") == [0, 15]
