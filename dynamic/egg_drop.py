import sys

#
# time: O(n_eggs * n_floors^2)
# space: O(n_eggs * n_floors)
# ref: https://youtu.be/iOaRjDT0vjc
#
def drop(n_eggs, n_floors) -> int:
    cache = [[0 for _ in range(n_floors + 1)]
             for _ in range(n_eggs + 1)]

    #
    # Base cases
    #
    # drop(n_eggs, 0) = 0
    # drop(0, n_floors) = 0

    # drop(n_eggs, 1) = 1
    for i in range(1, n_eggs + 1):
        cache[i][1] = 1

    # drop(1, n_floors) = n_floors
    for j in range(1, n_floors + 1):
        cache[1][j] = j

    #
    # Build up the memoize table
    #
    for i in range(2, n_eggs + 1):
        for j in range(2, n_floors + 1):
            cache[i][j] = sys.maxsize
            minimum = sys.maxsize

            # do simulation for each floor
            for x in range(1, j+1):
                minimum = min(minimum,
                              1 + max(
                                  # no break
                                  cache[i][j - x],
                                  # break
                                  cache[i - 1][x - 1]))

            cache[i][j] = minimum

    return cache[n_eggs][n_floors]


#
# time: O(n_eggs * log(n_floors))
# space: O(n_eggs * n_floors)
# ref: https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
#
def drop2(n_eggs, n_floors) -> int:
    cache = [[0 for _ in range(n_eggs + 1)]
             for _ in range(n_floors + 1)]

    n_moves = 0
    while cache[n_moves][n_eggs] < n_floors:
        n_moves += 1
        for k in range(1, n_eggs + 1):
            cache[n_moves][k] = 1 + \
                cache[n_moves - 1][k - 1] + \
                cache[n_moves - 1][k]

    return n_moves


def test_drop():
    assert(drop(1, 2) == 2)
    assert(drop(2, 6) == 3)
    assert(drop(3, 14) == 4)


def test_drop2():
    assert(drop2(1, 2) == 2)
    assert(drop2(2, 6) == 3)
    assert(drop2(3, 14) == 4)
