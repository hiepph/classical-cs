from typing import List, Optional
import math


def has_negative_weight_cycle(edges: List[List[int]], V: int) -> bool:
    """Adopt Bellman Ford's algorithm to detect negative weight cycles.

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
    start = 0

    dist[start] = 0
    for _ in range(V - 1):
        for (u, v, weight) in edges:
            if dist[v] > (dist[u] + weight):
                dist[v] = dist[u] + weight

    for (u, v, weight) in edges:
        if dist[v] > (dist[u] + weight):
            return True

    return False


def test():
    edges = [(0, 1, 4),
             (0, 2, 3),
             (1, 2, -2),
             (2, 3, -3),
             (2, 4, 1),
             (3, 1, 4),
             (3, 4, 2)]
    assert has_negative_weight_cycle(edges, 5)

    edges = [(0, 1, 4),
             (0, 3, 2),
             (1, 2, 2),
             (1, 3, 1),
             (1, 4, 3),
             (3, 1, 1),
             (3, 2, 4),
             (3, 4, 5),
             (4, 2, -5)]
    assert not has_negative_weight_cycle(edges, 5)
