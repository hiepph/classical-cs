T = dict()


def get_change(m, coins):
    if m not in T:
        T[m] = 0

        best = -1
        for coin in coins:
            if coin <= m:
                next_try = get_change(m - coin, coins)
                if best < 0 or best > next_try + 1:
                    best = next_try + 1
                    T[m] = best
    return T[m]


def test():
    coins = [1, 3, 4]
    assert get_change(2, coins) == 2
    assert get_change(34, coins) == 9
