# ref: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
#      https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
import networkx as nx
import matplotlib.pyplot as plt


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


def height_diff(root: TreeNode):
    return height(root.left) - height(root.right)


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


def delete(root: TreeNode, k):
    # normal deletion
    if not root:
        return root

    if k < root.val:
        root.left = delete(root.left, k)
    elif k > root.val:
        root.right = delete(root.right, k)
    else:
        if root.left is None:
            temp = root.right
            del root
            return temp

        if root.right is None:
            temp = root.left
            del root
            return temp

        temp = min_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    if root is None:
        return root

    # update the height of the ancestor node
    root = update_height(root)

    # rebalance
    return rebalance(root)


def rebalance(root: TreeNode):
    diff = height_diff(root)

    # left left
    if diff > 1 and height_diff(root.left) >= 0:
        return right_rotate(root)
    # right right
    if diff < -1 and height_diff(root.right) <= 0:
        return left_rotate(root)
    # left right
    if diff > 1 and height_diff(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # right left
    if diff < -1 and height_diff(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root


def min_node(root: TreeNode):
    """Left most leaf"""
    if root is None or root.left is None:
        return root
    return min_node(root.left)


def max_node(root: TreeNode):
    """Right most leaft"""
    if root is None or root.right is None:
        return root
    return max_node(root.right)


def preorder_print(root: TreeNode):
    if not root:
        return

    print(root.val, end=" ")
    preorder_print(root.left)
    preorder_print(root.right)


def merge_with_root(r1: TreeNode, r2: TreeNode, node: TreeNode):
    if abs(r1.height - r2.height) <= 1:
        node.left = r1
        node.right = r2
        r1.parent = node
        r2.parent = node
        node.height = max(r1.height, r2.height) + 1
        return node
    elif r1.height > r2.height:
        temp = merge_with_root(r1.right, r2, node)
        r1.right = temp
        temp.parent = r1
        return rebalance(r1)
    elif r1.height < r2.height:
        temp = merge_with_root(r1, r2.left, node)
        r2.left = temp
        temp.parent = r2
        return rebalance(r2)


def merge(r1: TreeNode, r2: TreeNode):
    node = max_node(r1)
    r1 = delete(r1, node.val)
    print(node.val)
    merge_with_root(r1, r2, node)
    return node


def r_visualize(G, root: TreeNode):
    G.add_node(root.val)
    if root.left is not None:
        G.add_edge(root.val, r_visualize(G, root.left))

    if root.right is not None:
        G.add_edge(root.val, r_visualize(G, root.right))
    return root.val


def visualize(root: TreeNode):
    G = nx.DiGraph()
    r_visualize(G, root)
    nx.planar_layout(G)
    nx.draw_networkx(G)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # insert
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    root = None
    for num in nums:
        root = insert(root, num)
    visualize(root)

    # delete
    root = delete(root, 10)
    visualize(root)

    # merge
    root2 = None
    for num in [16, 18]:
        root2 = insert(root2, num)
    visualize(root2)

    r = merge(root, root2)
    visualize(r)
