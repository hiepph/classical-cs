from typing import List, Optional
from queue import PriorityQueue
import math


def prim(G: List[List[Optional[int]]], start: int) -> (int, List[int]):
    """Prim algorithm for Mininum Spanning Tree (MST)

    Args:
        G: adjacency represented graph.
        start: the index of the vertex to start expanding from.

    Return:
        The total weight of the minimum spanning tree.
        List of the corresponding parent index (which shows the building path)
    """
    V = len(G)

    visited = [False] * V
    cost = [math.inf] * V
    parent = [None] * V
    q = PriorityQueue()

    cost[start] = 0
    for u in range(V):
        q.put((cost[u], u))
    while not q.empty():
        _, v = q.get()
        if visited[v]:
            continue

        visited[v] = True
        for z, weight in enumerate(G[v]):
            if weight and \
                (cost[z], z) in q.queue and cost[z] > weight:
                cost[z] = weight
                parent[z] = v
                q.put((cost[z], z))

    total_cost = 0
    for u in range(V):
        if parent[u] is not None:
            total_cost += G[u][parent[u]]

    return total_cost, parent


def test():
    #
    # Use adjacency matrix to represent a graph.
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

    total_weight, path = prim(G, 2)
    assert path == [1, 5, None, 0, 0, 2]
    assert total_weight == 14
