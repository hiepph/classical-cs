# refer: https://bit.ly/35lxhia
def kmp(s, pat):
    """
    Args:
    s: the source string
    pat: patttern to search

    Complexity:
    n: len(s)
    m: len(pat)
    time: O(n)

    Returns:
    id of first match
    """
    m = len(s)
    n = len(pat)

    table = state_transition(s)

    # the initial state of pat is 0
    cur_state = 0
    for i in range(n):
        cur_state = table[cur_state][s[i]]
        # if termination state is reached
        # the index at the beginning of the match is returned
        if cur_state == m:
            return i - m + 1

    # cannot reach the termination state, matching failed
    return -1

def state_transition(s):
    """build the state transition diagram:
    table[state][character] = next, where
        state: current state of the table
        character: character encountered
        next: represents the next state
    """


if __name__ == '__main__':
    assert kmp("aaacaaab", "aaab") == 4
    assert kmp("aaaaaaab", "aaab") == 4
