"""
We are given an unsorted array, nums, with n elements and each element is in the range [1,n] inclusive. The array originally contained all the elements from 1 to n
but due to a data error, one of the numbers is duplicated, which causes another number missing. Find and return the corrupt pair (missing, duplicated).

"""


def find_corrupt_pair(nums):
    missing = None
    duplicate = None

    i = 0
    n = len(nums)

    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i+1:
            duplicated = nums[i]
            missing = i+1

    return missing, duplicated