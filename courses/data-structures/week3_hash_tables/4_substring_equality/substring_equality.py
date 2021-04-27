import random
import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 10**9 + 7
        self.m2 = 10**9 + 9
        self.x = random.randrange(10**9) + 1
        n = len(s)

        self.h1 = [0] * (n + 1)
        for i in range(1, n + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(s[i - 1])) % self.m1
        self.h2 = [0] * (n + 1)
        for i in range(1, n + 1):
            self.h2[i] = (self.x * self.h2[i - 1] + ord(s[i - 1])) % self.m2

    def ask(self, a, b, l):
        hash1_a = self.h1[a + l] - self.x**l * self.h1[a]
        hash1_b = self.h1[b + l] - self.x**l * self.h1[b]

        hash2_a = self.h2[a + l] - self.x**l * self.h2[a]
        hash2_b = self.h2[b + l] - self.x**l * self.h2[b]
        return hash1_a % self.m1 == hash1_b % self.m1 \
            and hash2_a % self.m2 == hash2_b % self.m2


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s.strip())
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
