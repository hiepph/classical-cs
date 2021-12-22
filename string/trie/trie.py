def build_trie(patterns):
    """Build the trie from a list of patterns
    in the form of a dictionary of dictionaries.
    The key is node ID.
    The value is an internal dictionary which each key is an edge that
    points to one ID.

    Note: each pattern is concat with an additional '$' to mark the end
    of the string.

    Example: Assume  we have a list of patterns.
    + AT
    + AG
    + AC

    The trie would be:
    0->1: A
    1->4: C
    1->3: G
    1->2: T
    """
    trie = dict()

    i = 0
    for pattern in patterns:
        node = 0
        for ch in pattern:
            if node in trie and ch in trie[node]:
                node = trie[node][ch]
            else:
                i += 1
                if node not in trie:
                    trie[node] = dict()
                trie[node][ch] = i
                node = i
    return trie


def match(text, patterns):
    """Returns the list of indices
    that patterns are matched in the text."""
    patterns = list(map(lambda s: s + '$', patterns))
    trie = build_trie(patterns)

    result = []
    for i in range(len(text)):
        j = i
        node = 0
        while j < len(text) and text[j] in trie[node]:
            node = trie[node][text[j]]
            # if node not in trie:
            if '$' in trie[node]:
                result.append(i)
                break
            j += 1

    return result


def test():
    patterns = ["ATCG", "GGGT"]
    assert(match("AATCGGGTTCAATCGGGGT", patterns) == [1, 4, 11, 15])
