from collections import namedtuple
import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


Node = namedtuple('Node', ['key', 'level'])


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        # build the tree
        self.root = -1

        self.nodes = [[] for _ in range(self.n)]
        for k, parent_id in enumerate(self.parent):
            if parent_id == -1:
                self.root = k
            else:
                self.nodes[parent_id].append(k)
        # print(self.nodes)

    def compute_height(self):
        max_height = 1

        stack = []
        stack.append(Node(self.root, 1))
        while stack:
            node = stack.pop()
            for child in self.nodes[node.key]:
                stack.append(Node(child, node.level + 1))
                max_height = max(max_height, node.level + 1)
        return max_height


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
