from typing import List, Optional
import math
from queue import PriorityQueue


def dijkstra(edges: List[List[int]], V: int,
             start: int) -> (List[int], List[Optional[int]]):
    """
    Args:
        edges: List of (start, end, weight). Vertex index starts from 0.
        V: number of nodes
        start: vertice to calculate the distance from

    Returns:
        List of distances from current vertice to the start vertice
        List of parent vertices which is the previous visited vertice
        before current vertice
    """
    dist = [math.inf] * V
    prev = [None] * V
    dist[start] = 0

    q = PriorityQueue()
    for u in range(V):
        q.put((dist[u], u))

    while not q.empty():
        _, u = q.get()
        for (u, v, weight) in edges:
            if dist[v] > (dist[u] + weight):
                dist[v] = dist[u] + weight
                prev[v] = u
                q.put((dist[v], v))

    return dist, prev


def bellman_ford(G: List[List[Optional[int]]],
                 start: int) -> (List[int], List[Optional[int]]):
    V = len(G)

    dist = [math.inf] * V
    prev = [None] * V

    dist[start] = 0
    for _ in range(V - 1):
        pass


def test():
    # non-negative weights
    edges = [(0, 1, 3),
             (0, 3, 10),
             (1, 2, 3),
             (1, 3, 8),
             (1, 4, 5),
             (2, 3, 3),
             (2, 4, 1),
             (2, 5, 2),
             (3, 1, 2),
             (3, 4, 5),
             (4, 5, 0)]
    dist, prev = dijkstra(edges, 6, 0)
    assert dist == [0, 3, 6, 9, 7, 7]
    assert prev == [None, 0, 1, 2, 2, 4]

    # negative weights
