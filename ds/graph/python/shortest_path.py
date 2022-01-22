from typing import List, Optional
import math
from queue import PriorityQueue


def dijkstra(G: List[List[Optional[int]]],
             start: int) -> (List[int], List[Optional[int]]):
    """
    Returns:
        List of distances from current vertice to the start vertice
        List of parent vertices which is the previous visited vertice
        before current vertice
    """
    V = len(G)

    dist = [math.inf] * V
    prev = [None] * V

    dist[start] = 0

    q = PriorityQueue()
    for u in range(V):
        q.put((dist[u], u))

    while not q.empty():
        _, u = q.get()
        for v, weight in enumerate(G[u]):
            if weight is None:
                continue

            if dist[v] > (dist[u] + weight):
                dist[v] = dist[u] + weight
                prev[v] = u
                q.put((dist[v], v))

    return dist, prev


def bellman_ford():
    pass


def test():
    """Graph is represented as an adjacency matrix where
    G[u][v] indicates the direction from u -> v and has weight G[u][v].

    G[u][v] == None means no edge.
    """
    # non-negative weights
    G = [[None, 3, None, 10, None, None],
         [None, None, 3, 8, 5, None],
         [None, None, None, 3, 1, 2],
         [None, 2, None, None, 5, None],
         [None, None, None, None, None, 0],
         [None, None, None, None, None, None]]
    dist, prev = dijkstra(G, 0)
    assert dist == [0, 3, 6, 9, 7, 7]
    assert prev == [None, 0, 1, 2, 2, 4]

    # negative weights
