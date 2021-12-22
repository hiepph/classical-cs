class Node(object):
    def __init__(self, label):
        self.label = label
        self.out = dict()


class SuffixTree(object):
    """
    Suffix Tree in which:
    + edges contain the character paths that lead to nodes
    + nodes contain the substrings that can'be branched off

    For example, 'A$' would become:
    |nil| --A--> |A$|
          --$--> |$|

    'ACA$' woulde become:
    |nil| --A--> |A| --C--> CA$
                     --$--> $
          --C--> CA$
          --$--> $


    The nodes of the suffix tree represents the edges of a
    suffix tree in theory.
    For example, 'ACA$' in theory is:
    |-| --A--> |-| --CA$--> |-|
                   --$----> |-|
        -CA$-> |-|
        --$--> |-|
    """

    def __init__(self, text):
        text = text + '$'
        self.root = Node(None)
        self.root.out[text[0]] = Node(text)
        for i in range(1, len(text)):
            cur = self.root
            j = i
            while j < len(text):
                if text[j] in cur.out:
                    child = cur.out[text[j]]
                    label = child.label
                    # walk until we need to branch 2 new subtrees
                    k = j + 1
                    while k - j < len(label) and text[k] == label[k - j]:
                        k += 1
                    if k - j == len(label):
                        cur = child
                        j = k
                    else:
                        label1, label2 = label[k - j], text[k]
                        # new node to connect 2 new branches
                        bisect_node = Node(label[:k - j])
                        bisect_node.out[label2] = Node(text[k:])
                        bisect_node.out[label1] = Node(label[k - j:])
                        cur.out[text[j]] = bisect_node
                else:
                    cur.out[text[j]] = Node(text[j:])

    def print_edges(self):
        """Print out all the edges of the theoretical suffix tree"""
        self.print_edges_recur(self.root)

    def print_edges_recur(self, node: Node):
        for child in node.out:
            print(node.out[child].label)
            self.print_edges_recur(node.out[child])

    def has_substring(self, pattern) -> bool:
        """
        Returns whether the pattern is found
        """
        cur = self.root
        i = 0
        while i < len(pattern):
            c = pattern[i]
            if c not in cur.out:
                return False
            child = cur.out[pattern[i]]
            label = child.label
            j = i + 1
            while j - i < len(label) \
                    and j < len(pattern) \
                    and pattern[j] == label[j - i]:
                j += 1
            if j - i == len(label):
                cur = child
                i = j
            elif j == len(pattern):
                return True
            else:
                return False

        return False


def test():
    tree = SuffixTree("You shall not pass!")
    # tree.print_edges()

    assert(tree.has_substring("pass"))
    assert(not tree.has_substring("yes"))
