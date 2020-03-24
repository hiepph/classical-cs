def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return a*b / gcd(a, b)


def test_lcm():
    assert lcm(6, 8) == 24
    assert lcm(761457, 614573) == 467970912861
