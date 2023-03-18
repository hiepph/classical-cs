def lis(A, seq):
    result = len(seq)

    # start with an empty sequence
    if len(seq) == 0:
        last_index = -1
        last_element = float('-inf')
    else:
        last_index = seq[-1]
        last_element = A[last_index]

    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            # extend element by element (a larger number) recursively
            result = max(result, lis(A, seq + [i]))

    return result


# Optimise: we're not using all of the sequence.
# We're only interested in its last element and its length.
def lis2(A, seq_len, last_index):
    if last_index == -1:
        last_element = float('-inf')
    else:
        last_element = A[last_index]

    result = seq_len

    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, lis2(A, seq_len + 1, i))

    return result


# Optimise: we don't even need seq_len
def lis3(A, last_index):
    if last_index == -1:
        last_element = float('-inf')
    else:
        last_element = A[last_index]

    result = 0

    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, 1 + lis3(A, i))

    return result


# Now it remains to add memoisation: check `iterative.py` or `recursion.py`


if __name__ == '__main__':
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
    assert lis(A, []) == 5

    assert lis2(A, 0, -1) == 5

    assert lis3(A, -1) == 5
