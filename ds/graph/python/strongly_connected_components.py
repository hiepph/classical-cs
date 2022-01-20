from typing import List, Optional, Set


def dfs(G: List[List[int]], visited: List[bool], order: List[int], u: int):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs(G, visited, order, v)
    order.append(u)


def toposort(G: List[List[int]]) -> List[int]:
    """

    Args:
        G: adjacent list format

    Returns:
        The vertices sorted topologically
    """
    V = len(G)

    visited = [False] * V
    order = []

    for u in range(V):
        if not visited[u]:
            dfs(G, visited, order, u)

    order.reverse()
    return order


def graph_reverse(G: List[List[int]]) -> List[List[int]]:
    """Return a new graph with all edges reversed"""
    rev = [[] for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            rev[v].append(u)

    return rev


def explore(G: List[List[int]], visited: List[bool], group: List[int], u: int):
    """DFS without tracking order"""
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            explore(G, visited, group, v)

    group.append(u)


def ssc(G: List[List[int]]) -> Set[List[int]]:
    """Detect the strongly connected components in the graph

    Args:
        G: adjacent list representation

    Returns:
        Set of lists which contains strongly connected vertices (sorted by vertices)
    """
    rev = graph_reverse(G)

    visited = [False] * len(G)
    result = set()
    for u in toposort(rev):
        group = []
        if not visited[u]:
            explore(G, visited, group, u)
        if group:
            result.add(tuple(sorted(group)))

    return result


def test():
    #
    # Graph is represented as an adjacent list
    # G[u] contains the vertices that u is pointing to
    #
    G = [[1],
         [4, 5],
         [1],
         [0, 6],
         [0, 2],
         [],
         [7],
         [8],
         [5, 7]]

    assert ssc(G) == {(0, 1, 2, 4), (3,), (5,), (6,), (7, 8)}
