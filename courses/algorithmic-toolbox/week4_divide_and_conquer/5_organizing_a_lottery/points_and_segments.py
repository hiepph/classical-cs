# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # your code here
    l = []
    l += [(start, 'l') for start in starts]
    l += [(end, 'r') for end in ends]
    l += [(point, 'p') for point in points]

    l = sorted(l)

    d = {}
    segment_count = 0
    for t in l:
        if t[1] == 'l':
            segment_count += 1
        elif t[1] == 'r':
            segment_count -= 1
        else:  # 'p'
            d[t[0]] = segment_count

    for i, p in enumerate(points):
        cnt[i] = d[p]
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def test():
    assert fast_count_segments([0, 7], [5, 10], [1, 6, 11]) == [1, 0, 0]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
