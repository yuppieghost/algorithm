from typing import List


def bsearch(nums: List, target) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
