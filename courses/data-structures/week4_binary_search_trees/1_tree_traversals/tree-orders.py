# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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

  def inOrderRecur(self, res, root):
    if root == -1:
      return

    self.inOrderRecur(res, self.left[root])
    res.append(self.key[root])
    self.inOrderRecur(res, self.right[root])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inOrderRecur(self.result, 0)
    return self.result

  def preOrderRecur(self, res, root):
    if root == -1:
      return

    res.append(self.key[root])
    self.preOrderRecur(res, self.left[root])
    self.preOrderRecur(res, self.right[root])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrderRecur(self.result, 0)
    return self.result

  def postOrderRecur(self, res, root):
    if root == -1:
      return

    self.postOrderRecur(res, self.left[root])
    self.postOrderRecur(res, self.right[root])
    res.append(self.key[root])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrderRecur(self.result, 0)
    return self.result

def main():
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
