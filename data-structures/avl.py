# ref: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

class TreeNode:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 1


def height(node: TreeNode):
    return node.height if node else 0


def update_height(node: TreeNode):
    node.height = 1 + max(height(node.left), height(node.right))
    return node


def insert(root: TreeNode, k):
    # normal insertion
    if not root:
        return TreeNode(k)
    if k < root.val:
        root.left = insert(root.left, k)
    else:
        root.right = insert(root.right, k)

    # update height
    root = update_height(root)

    # (left - right) height difference
    diff = height(root.left) - height(root.right)

    # left left case
    if diff > 1 and k < root.left.val:
        return right_rotate(root)

    # right right case
    if diff < -1 and k > root.right.val:
        return left_rotate(root)

    # left right case
    if diff > 1 and k > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # right left case
    if diff < -1 and k < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


#
#   x                     y
#  / \       left        / \
# T1  y      ----->     x  T3
#    / \     <----     / \
#   T2 T3    right    T1 T2
#


def left_rotate(x: TreeNode):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x = update_height(x)
    y = update_height(y)

    return y


def right_rotate(y: TreeNode):
    x = y.left
    T2 = x.right

    y.left = T2
    x.right = y

    y = update_height(y)
    x = update_height(x)

    return x


def preorder_print(root: TreeNode):
    if not root:
        return

    print(root.val, end=" ")
    preorder_print(root.left)
    preorder_print(root.right)


if __name__ == '__main__':
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)
    preorder_print(root)
