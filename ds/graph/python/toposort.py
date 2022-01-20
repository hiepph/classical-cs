from typing import List, Optional


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


def test():
    #
    # Graph is represented as an adjacent list
    # G[u] contains the vertices that u is pointing to
    #
    G = [[1, 3, 4],
         [2],
         [3],
         [],
         [3]]

    assert(toposort(G) == [0, 4, 1, 2, 3])
