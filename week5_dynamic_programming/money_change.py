import math
import functools

coins = [1, 5, 10, 25]
@functools.lru_cache(None)
def change(n):
    if n == 0:
        return 0
    best = -1
    for coin in coins:
        if coin <= n:
            next_try = change(n-coin)
        if best < 0 or best > next_try + 1:
            best = next_try + 1
    return best


def dpchange(money, coins):
    min_num_coins = [math.inf] * (money + 1)
    min_num_coins[0] = 0
    for m in range(1, money+1):
        for coin in coins:
            if m >= coin:
                n_coins = min_num_coins[m-coin] + 1
                if n_coins < min_num_coins[m]:
                    min_num_coins[m] = n_coins
    return min_num_coins[money]


def test():
    assert change(5) == 1
    assert change(76) == 4

    assert dpchange(5, coins) == 1
    assert dpchange(76, coins) == 4
