from typing import List, Set


def activity_selection(A: List[str], s: List[int], f: List[int]) -> Set[str]:
    indices = sorted(range(len(f)), key=lambda k: f[k])

    S = {A[indices[0]]}
    k = indices[0]

    for i in indices[1:]:
        if s[i] >= f[k]:
            S.add(A[i])
            k = i

    return S


def test():
    # activity names
    A = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']

    # start times
    s = [5, 1, 3, 0, 5, 8]

    # finish times
    f = [9, 2, 4, 6, 7, 9]

    assert activity_selection(A, s, f) == {'a2', 'a3', 'a5', 'a6'}
