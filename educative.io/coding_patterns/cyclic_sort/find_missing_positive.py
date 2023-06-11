"""
Given an unsorted integer array, nums, return the smallest missing positive integer. Create an algorithm that runs with an O(n)
time complexity and utilizes a constant amount of space.
"""


def smallest_missing_positive_integer(nums):
    n = len(nums)
    i = 0

    while i < n:
        j = nums[i]-1
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n + 1