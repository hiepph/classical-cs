#
# ref: https://youtu.be/iOaRjDT0vjc
#
import sys

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


if __name__ == '__main__':
    assert(drop(1, 2) == 2)
    assert(drop(2, 6) == 3)
    assert(drop(3, 14) == 4)
