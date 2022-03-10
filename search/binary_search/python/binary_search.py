from typing import List


def binary_search(nums: List[int], target: int):
    """Binary search for a *sorted* array"""
    return bs(nums, target, 0, len(nums) - 1)


def bs(nums: List[int], target: int, low: int, high: int):
    while low <= high:
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def test():
    assert binary_search([1, 2, 8, 9, 12], 8) == 2
    assert binary_search([1, 2, 8, 9], 8) == 2
    assert binary_search([8, 12, 14], 8) == 0
    assert binary_search([8, 12, 14], 9) == -1
