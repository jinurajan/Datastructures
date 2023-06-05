"""
Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

1 <= nums.length <= 5000
-pow(10,4) <= nums[i] <= pow(10,4)
All values of nums are unique
nums is an ascending array that is possibly rotated
-pow(10,4) <= target <= pow(10,4)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid +1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def find_rotated_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                else:
                    if nums[mid] < nums[left]:
                        right = mid-1
                    else:
                        left = mid+1
        def bs(left, right, target):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return bs(mid+1, right, target)
            else:
                return bs(left, mid-1, target)
        
        n = len(nums)
        if n==1:
            return 0 if nums[0] == target else -1
        rotate_index = find_rotated_index(0, n-1)

        if nums[rotate_index] == target:
            return rotate_index
        
        if rotate_index == 0:
            return bs(0, n-1, target)
        if target < nums[0]:
            return bs(rotate_index, n-1, target)

        return bs(0, rotate_index, target)
    


