# python3
import sys


def compute_min_refills(distance, tank, stops):
    if tank > distance:
        return 0

    c = 0  # the initial position
    count = 0

    while c < distance:
        # get as far as we can
        c += tank

        if len(stops) > 0:
            # update current position to the (left) nearest stops
            while stops and c >= stops[0]:
                nearest_stop = stops.pop(0)
            c = nearest_stop
            count += 1

            # impossible case
            if stops and c + tank < stops[0]:
                return -1

    return count


def test():
    assert compute_min_refills(950, 400, [200, 375, 550, 750]) == 2
    assert compute_min_refills(10, 3, [1, 2, 5, 9]) == -1
    assert compute_min_refills(200, 250, [100, 150]) == 0


if __name__ == '__main__':
    # compute_min_refills(950, 400, [200, 375, 550, 750])
    compute_min_refills(10, 3, [1, 2, 5, 9])
