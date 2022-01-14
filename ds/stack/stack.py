from collections import deque


class Stack:
    def __init__(self):
        self.data = deque()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return not bool(self.data)
