class TreeNode:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
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


def left_descendant(root: TreeNode):
    if not root.left:
        return root
    return left_descendant(root.left)


def right_ancestor(root: TreeNode):
    if not root:
        return None
    if root.val < root.parent.val:
        return root.parent
    return right_ancestor(root.parent)


def next(root: TreeNode):
    # return the next largest node
    if root.right:
        return left_descendant(root.right)
    return right_ancestor(root)


def range_search(l, h, root: TreeNode):
    result = []
    n = find(l, root)
    while root.val <= h:
        if root.val >= l:
            result.append(n)
        n = next(n)
    return result


def insert(k, root: TreeNode):
    p = find(k, root)
    new_node = TreeNode(val=k, parent=p)

    if p.val == k:
        return p
    elif p.val < k:
        p.right = new_node
    else:
        p.left = new_node


def delete(root: TreeNode):
    if not root.right:
        # remove root, promote root.left
        root = root.left
    else:
        x = next(root)  # note: x.left == None
        # replace root by x, promote x.right
        root = x
        x = x.right
