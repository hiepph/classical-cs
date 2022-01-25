from queue import PriorityQueue
from collections import Counter
from typing import Dict


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(frequency: Dict[str, int]) -> TreeNode:
    q = PriorityQueue()
    for c, freq in frequency.items():
        q.put((freq, TreeNode(c)))

    while q.qsize() > 1:
        l_freq, l = q.get()
        r_freq, r = q.get()
        q.put((l_freq + r_freq, TreeNode(None, l, r)))

    _, root = q.get()
    return root


def huff(root: TreeNode, path: str, code: Dict[str, str]):
    if root.left is None and root.right is None:
        code[root.val] = path
    if root.left:
        huff(root.left, path + "0", code)
    if root.right:
        huff(root.right, path + "1", code)


def encode(text: str) -> (Dict[str, int], Dict[str, str]):
    """
    1. Count the frequency of characters
    2. Generate Binary Tree
    3. Generate binary code from the tree

    Returns:
        Frequency of each char
        Huffman coding for each char
    """
    frequency = Counter(text)
    root = generate_tree(frequency)

    code = dict()
    huff(root, "", code)
    return frequency, code


def test():
    text = "BCAADDDCCACACAC"

    freq, huff = encode(text)
    assert freq == {'A': 5,
                    'B': 1,
                    'C': 6,
                    'D': 3}
    assert huff == {'A': "11",
                    'B': "100",
                    'C': "0",
                    'D': "101"}
