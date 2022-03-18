def kmp(text, pattern):
    """Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    S = pattern + '$' + text
    table = compute_prefix_table(S)

    result = []
    for i in range(len(pattern) + 1, len(S)):
        if table[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result


def compute_prefix_table(P):
    table = [0] * len(P)
    border = 0
    for i in range(1, len(P)):
        while border > 0 and P[i] != P[border]:
            border = table[border - 1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        table[i] = border

    return table


def test():
    assert kmp("GT", "TACG") == []
    assert kmp("ATATA", "ATA") == [0, 2]
    assert kmp("GATATATGCATATACTT", "ATAT") == [1, 3, 9]

    assert kmp("Hello, $World$!", "$") == [7, 13]
