"""
Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.


Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            # not rotated
            return nums[0]

        def find_rotate_index(left, right):
            if left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[mid+1]:
                    return nums[mid + 1]
                if nums[mid-1] > nums[mid]:
                    return nums[mid]

                if nums[mid] > nums[0]:
                    # look on the right
                    return find_rotate_index(mid+1, right)
                else:
                     return find_rotate_index(left, mid-1)

        return find_rotate_index(0, len(nums)-1)
    


array = [7,8,1,2,3,4,5,6]
print(Solution().findMin(array))

array = [1,2,3,4,5,6]
print(Solution().findMin(array))

array = [4,5,6,7,8,1,2,3]
print(Solution().findMin(array))

array = [4,5,6,7,8,0,2,3]
print(Solution().findMin(array))