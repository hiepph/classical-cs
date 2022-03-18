def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def test():
    assert gcd(8, 6) == 2
