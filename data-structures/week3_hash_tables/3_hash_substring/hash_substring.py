def polyhash(s):
    _multiplier = 263
    _prime = 1000000007

    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # Rabin Karp algorithm
    pattern_hash = polyhash(pattern)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if polyhash(text[i:i + len(pattern)]) == pattern_hash
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
