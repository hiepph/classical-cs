# Uses python3
import sys
import math
from operator import itemgetter


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def minimum_distance(points):
    # write your code here
    if len(points) == 2:
        return dist(points[0], points[1])

    if len(points) == 3:
        return min(dist(points[0], points[1]),
                   dist(points[0], points[2]),
                   dist(points[1], points[2]))

    points = sorted(points)  # sort by x
    n = len(points)
    # split subsets
    S1 = points[:n // 2]
    S2 = points[n // 2:]
    # recursive call to get min distance of each subset
    d1 = minimum_distance(S1)
    d2 = minimum_distance(S2)

    # filter x-dist which does not exceed d
    d = min(d1, d2)

    xd = (S1[-1][0] + S2[0][0]) // 2
    roi = []
    for p in S1 + S2:
        if abs(p[0] - xd) <= d:
            roi.append(p)

    roi = sorted(roi, key=itemgetter(1))  # sort by y
    # get min distance to 7 subsequent points
    _d = d
    for i in range(len(roi) - 1):
        for j in range(i + 1, min(i + 1 + 7, len(roi))):
            dij = dist(roi[i], roi[j])
            _d = min(dij, _d)

    return _d


def test():
    import pytest
    assert minimum_distance([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0),
                             (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]) \
        == pytest.approx(1.414213)
    assert minimum_distance([(7, 7), (1, 100), (4, 8), (7, 7)]) == 0.0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    print("{0:.9f}".format(minimum_distance(points)))
