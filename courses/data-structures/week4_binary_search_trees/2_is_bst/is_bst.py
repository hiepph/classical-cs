#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order_recur(self, res, root):
        if root == -1:
            return

        self.in_order_recur(res, self.left[root])
        res.append(self.key[root])
        self.in_order_recur(res, self.right[root])

    def is_bst_recur(self, root):
        if root == -1:
            return True
        res = True
        if self.left[root] != -1:
            res = res and \
                self.key[root] > self.key[self.left[root]] and \
                self.is_bst_recur(self.left[root])
        if self.right[root] != -1:
            res = res and \
                self.key[root] < self.key[self.right[root]] and \
                self.is_bst_recur(self.right[root])
        return res

    def is_bst(self):
        # sanity check
        # don't care about value of sub-child compared to current root
        sanity_check = self.is_bst_recur(0)
        if not sanity_check:
            return False

        # do in-order traversal
        # if the result is not sorted, then it's not a valid bst tree
        in_order = []
        self.in_order_recur(in_order, 0)
        for i in range(len(in_order) - 1):
            if in_order[i] >= in_order[i + 1]:
                return False

        return True


def main():
    tree = TreeOrders()
    tree.read()
    if tree.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
