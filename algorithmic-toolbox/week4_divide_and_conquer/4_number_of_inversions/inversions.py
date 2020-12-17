# Uses python3
import sys


def merge(a, b, left, ave, right):
    b = a
    L = b[left:ave + 1]
    R = b[ave + 1:right + 1]

    # count pairs
    number_of_inversions = 0
    for ir in range(len(R)):
        for il in range(len(L)):
            if L[il] > R[ir]:
                number_of_inversions += 1

    # merge
    il = ir = 0
    ia = left
    # copy value of subarrays back to a
    while il < len(L) and ir < len(R):
        if L[il] < R[ir]:
            a[ia] = L[il]
            il += 1
        else:
            a[ia] = R[ir]
            ir += 1
        ia += 1

    # copy left values of L/R
    while il < len(L):
        a[ia] = L[il]
        ia += 1
        il += 1
    while ir < len(R):
        a[ia] = R[ir]
        ia += 1
        ir += 1

    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here

    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions


def test():
    a = [2, 3, 9, 2, 9]
    assert get_number_of_inversions(
        a, len(a) * [0], 0, len(a)) == 2


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
