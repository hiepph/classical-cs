from typing import List
import queue


def is_bipartite(graph: List[List[int]]) -> bool:
    RED = 0
    BLUE = 1

    q = queue.Queue()

    colors = [None for _ in range(len(graph))]
    for u in range(len(graph)):
        if colors[u]:
            continue

        colors[u] = RED
        q.put(u)
        while not q.empty():
            s = q.get()
            for t in graph[s]:
                if not colors[t]:
                    colors[t] = BLUE if colors[s] == RED else RED
                    q.put(t)

                if colors[s] == colors[t]:
                    return False

    return True


def test():
    #
    # graph: adjacency list representation
    #
    assert is_bipartite([[1,3],[0,2],[1,3],[0,2]])
    assert not is_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
