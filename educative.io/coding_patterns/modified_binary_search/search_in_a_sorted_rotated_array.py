"""
Given a sorted integer array, nums, and an integer value, target, the array is rotated by some arbitrary number. Search and return the index of target in this array. If the target does not exist, return -1.
"""

def bs(nums, low, high, target):
    if low > high:
        return -1
    mid = low + (high-low) // 2

    if nums[mid] == target:
        return mid
    if nums[low] <= nums[mid]:
        if nums[low] <= target and target < nums[mid]:
            return bs(nums, low, mid-1, target)
        return bs(nums, mid+1, high, target)
    else:
        if nums[mid] <= target and target < nums[high]:
            return bs(nums, mid+1, high, target)
        return bs(nums, low, mid-1, target)


def binary_search(nums, target):
    return bs(nums, 0, len(nums)-1, target)
    

def main():
    target_list = [3, 6, 3, 6]
    nums_list = [[6, 7, 1, 2, 3, 4, 5], [6, 7, 1, 2, 3, 4, 5],
                 [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3]]

    for i in range(len(target_list)):
        print((i + 1), ".\tRotated array: ", nums_list[i], "\n\ttarget", target_list[i], "found at index ", \
              binary_search(nums_list[i], target_list[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
