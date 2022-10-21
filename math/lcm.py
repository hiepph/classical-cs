from gcd import gcd

def lcm(a, b):
    return a * b / gcd(a, b)

def test():
    assert lcm(8, 6) == 24
