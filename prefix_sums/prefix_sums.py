from typing import List


def prefix_sums(A: List[int]) -> List[int]:
    """Or rolling sum"""
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def prefix_sums_with_limit(A: List[int], limit=10**9) -> (List[int], bool):
    """Prefix sums with early stopping.
    The second result returns whether the prefix sums calculation
    completes before reaching limit."""
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
        if P[k] > limit:
            return P, False
    return P, True


def count_total(P: List[int], x: int, y: int) -> int:
    """Calculate the total of any slice [x..y] of the array quickly.
    Naive: Recalculate each slice repeatedly. O(nm)
    prefix sums: O(1) for a calcuation. Total: O(n + m).
    P is already constructed with O(n), plus additional m calculations."""
    return P[y + 1] - P[x]


def test_prefix_sums():
    assert prefix_sums([1, 3, 4, 5]) == [0, 1, 4, 8, 13]


def test_count_total():
    pref = prefix_sums([1, 3, 4, 5])

    assert count_total(pref, 1, 2) == 7
    assert count_total(pref, 1, 3) == 12
