"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_idx = 0
        for idx, n in enumerate(nums):
            if n != 0:
                nums[start_idx], nums[idx] = nums[idx], nums[start_idx]
                start_idx += 1
        return nums



nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))





