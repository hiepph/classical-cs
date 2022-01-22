def dfs_has_back_edge(G, start, visited, finished) -> bool:
    """DFS and returns whether back edge existed
    """
    if finished[start]:
        return False

    if visited[start]:
        return True

    visited[start] = True
    for v in G[start]:
        if dfs_has_back_edge(G, v, visited, finished):
            return True

    finished[start] = True
    return False


def has_cycle(G) -> bool:
    V = len(G)

    visited = [False] * V
    finished = [False] * V
    for u in range(V):
        if dfs_has_back_edge(G, u, visited, finished):
            return True

    return False


def test():
    # adjacency list representation
    G1 = [[1, 6, 7],
         [2, 5],
         [3, 4],
         [],
         [],
         [],
         [],
         [8, 11],
         [9, 10],
         [],
         [8],
         [10]]
    assert has_cycle(G1)

    G2 = [[1, 6, 7],
         [2, 5],
         [3, 4],
         [],
         [],
         [],
         [],
         [8, 11],
         [9, 10],
         [],
         [],
         [10]]
    assert not has_cycle(G2)
