def rabinkarp(text, pattern, multiplier=263, prime=1000000007):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return [0]

    if m > n:
        return []

    res = []

    hash_pattern = hash_text = 0
    for i in range(m):
        hash_pattern = (hash_pattern * multiplier + ord(pattern[i])) % prime
        hash_text = (hash_text * multiplier + ord(text[i])) % prime

    h = pow(multiplier, m - 1, prime)

    for i in range(n - m + 1):
        if hash_text == hash_pattern:
            if pattern == text[i : i + m]:
                res.append(i)
        if i < n - m:
            hash_text = (
                (hash_text - ord(text[i]) * h) * multiplier + ord(text[i + m])
            ) % prime

            if hash_text < 0:
                hash_text += prime

    return res


def test():
    assert rabinkarp("GT", "TACG") == []
    assert rabinkarp("ATATA", "ATA") == [0, 2]
    assert rabinkarp("GATATATGCATATACTT", "ATAT") == [1, 3, 9]

    assert rabinkarp("Hello, $World$!", "$") == [7, 13]
