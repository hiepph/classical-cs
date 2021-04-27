import math
import sys
from collections import namedtuple

Item = namedtuple('Item', ['value', 'max'])

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Top(self):
        return self.__stack[-1]

    def Push(self, a):
        if len(self.__stack) == 0:
            item = Item(a, a)
        else:
            item = Item(a, max(self.Top().max, a))
        self.__stack.append(item)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.Top().max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
