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


def print_edges(result, node):
    """Print the edges of theoretical suffix tree"""
    for child in node.out:
        print(node.out[child].label)
        collect(result, node.out[child])


def test():
    tree = SuffixTree("ACA")
