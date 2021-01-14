def set_bit(x, pos):
    mask = 1 << pos
    return x | mask


def clear_bit(x, pos):
    mask = 1 << pos
    return x & ~mask


def flip_bit(x, pos):
    mask = 1 << pos
    return x ^ mask


def is_bit_set(x, pos):
    shifted = x >> pos
    return shifted & 1


def is_even(x):
    return x & 1 == 0


def is_power_of_two(x):
    return x & (x - 1) == 0


def last_bit(x):
    # or x & ~(x-1)
    return x & -x


def remove_last_bit(x):
    return x & (x - 1)


def test():
    x = int('00000110', 2)
    assert set_bit(x, 5) == int('00100110', 2)

    x = int('01100110', 2)
    assert clear_bit(x, 5) == int('01000110', 2)

    x = int('01000110', 2)
    assert flip_bit(x, 5) == int('01100110', 2)

    x = int('01100110', 2)
    assert is_bit_set(x, 5)

    x = 4
    assert is_even(x)

    x = int('1000', 2)
    assert is_power_of_two(x)

    x = int('0111', 2)
    assert last_bit(x) == 1
