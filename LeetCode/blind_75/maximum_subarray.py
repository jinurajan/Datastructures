"""
Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""

from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer

        def find_best_subarray(nums, left, right):
            if left > right:
                return -math.inf
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
            
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            left_half = find_best_subarray(nums, left, mid-1)
            right_half =find_best_subarray(nums, mid+1, right)

            return max(best_combined_sum, left_half, right_half)
        
        return find_best_subarray(nums, 0, len(nums)-1)
        


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorithm
        current_sub_sum = nums[0]
        max_sub_sum = nums[0]
        
        for idx in range(1, len(nums)):
            current_sub_sum = max(current_sub_sum+nums[idx], nums[idx])
            max_sub_sum = max(max_sub_sum, current_sub_sum)
        return max_sub_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray