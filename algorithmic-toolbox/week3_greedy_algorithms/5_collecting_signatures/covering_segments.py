# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x[1])  # sort by right end
    i = 0
    n = len(segments)
    while i < n:
        cur = segments[i]
        # loop while end of current segment overlap next segments
        while i < n - 1 and cur[1] >= segments[i + 1][0]:
            i += 1
        points.append(cur[1])
        i += 1

    return points


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *data = map(int, input.split())
    # segments = list(map(lambda x: Segment(
    #     x[0], x[1]), zip(data[::2], data[1::2])))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)

    print(optimal_points([[1, 3], [2, 5], [3, 6]]))
    print(optimal_points([[4, 7], [1, 3], [2, 5], [5, 6]]))
