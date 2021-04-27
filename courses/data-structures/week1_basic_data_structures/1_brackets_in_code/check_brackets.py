import os
from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            new_open = Bracket(char=next, position=i + 1)
            opening_brackets_stack.append(new_open)
        if next in ")]}":
            new_closed = Bracket(char=next, position=i + 1)
            if not opening_brackets_stack:
                return new_closed.position
            while opening_brackets_stack:
                top = opening_brackets_stack.pop()
                if are_matching(top.char, new_closed.char):
                    break
                return new_closed.position

    if opening_brackets_stack:
        return opening_brackets_stack.pop().position
    return "Success"


def test():
    for i in range(1, len(os.listdir("tests")) // 2 + 1):
        inp = open("tests/" + str(i).zfill(2)).read().strip()

        res = find_mismatch(inp)
        target = open("tests/" + str(i).zfill(2) + ".a").read().strip()

        assert str(res) == target, f"test: {i}, input: {inp}"
