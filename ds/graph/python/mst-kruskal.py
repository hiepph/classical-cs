from typing import List, Optional, Tuple, Set


class UnionQuickFind():
    def __init__(self, N: int):
        """Initialize the union-find data structure"""
        self.ids = [i for i in range(N)]

    def connected(self, p, q: int) -> bool:
        """check if p and q are connected
        """
        return self.ids[p] == self.ids[q]

    def union(self, p, q: int):
        """add the connection between p and q
        """
        pid = self.ids[p]
        qid = self.ids[q]

        # change all entries with ids[p] to ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid


def extract_edges(G: List[List[Optional[int]]]) -> List[Tuple[Tuple[int, int], int]]:
    """Extract the edges together with weights from the representation of graph
    """
    V = len(G)
    edges = []
    for u in range(V):
        for v in range(u + 1, V):
            weight = G[u][v]
            if weight:
                edges.append(((u, v), weight))
    return edges


def kruskal(G: List[List[Optional[int]]], start: int) -> (int, Set[Tuple[int, int]]):
    """Kruskal algorithm for Mininum Spanning Tree (MST)

    Args:
        G: adjacency represented graph.
        start: the index of the vertex to start expanding from.

    Return:
        The total weight of the minimum spanning tree.
        Set of edges that connect together in MST.
    """
    edges = extract_edges(G)
    sorted_edges = sorted(edges, key=lambda item: item[1])

    V = len(G)
    union = UnionQuickFind(V)
    parent = [None] * V

    path = set()
    for i, ((u, v), w) in enumerate(sorted_edges):
        if not union.connected(u, v):
            path.add((u, v))
            union.union(u, v)

    total_weight = 0
    for (u, v) in path:
        total_weight += G[u][v]
    return total_weight, path


def test():
    #
    # Use adjacency matrix to represent an undirected graph.
    #
    # G[i][j] is the weight from vertex i to vertex j.
    # None means no connection between 2 vertices.
    #
    G = [[0, 4, None, 2, 1, None],
         [4, 0, 8, None, 5, 6],
         [None, 8, 0, None, None, 1],
         [2, None, None, 0, 3, None],
         [1, 5, None, 3, None, 9],
         [None, 6, 1, None, 9, 0]]

    total_weight, path = kruskal(G, 2)
    assert path == {(0, 1), (0, 3), (0, 4), (1, 5), (2, 5)}
    assert total_weight == 14
