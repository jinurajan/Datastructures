"""
You are required to find an integer t in an array arr of non-distinct integers. Prior to being passed as input to your search function, arr has been processed as follows:

It has been sorted in non-descending order.
It has been rotated around some pivot k such that, after rotation, it looks like this: [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. For example, [10, 30, 40, 42, 42, 47, 78, 90, 901], rotated around pivot k=5 becomes [47, 78, 90, 901, 10, 30, 40, 42, 42].
Return TRUE if t exists in the rotated, sorted array arr, and FALSE otherwise, while minimizing the number of operations in the search.
"""

def binary_search(nums, low, high, target):

    if (low > high):
        return False
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return True

    if nums[low] <= nums[mid]:
        if nums[low] <= target and target < nums[mid]:
            return binary_search(nums, low, mid-1, target)
        return binary_search(nums, mid+1, high, target)
    else:
        if nums[mid] < target and target <= nums[high]:
            return binary_search(nums, mid+1, high, target)
        return binary_search(nums, low, mid-1, target)


def search(arr, t):
    return binary_search(arr, 0, len(arr)-1, t)

