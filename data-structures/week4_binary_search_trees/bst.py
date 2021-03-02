class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find(k, root: TreeNode):
    if root.val == k:
        return root
    elif root.val > k:
        if root.left is not None:
            return find(k, root.left)
        return root
    elif root.val < k:
        return find(k, root.right)


def next(root: TreeNode):
    # return the next largest node
    pass


if __name__ == '__main__':
    pass
