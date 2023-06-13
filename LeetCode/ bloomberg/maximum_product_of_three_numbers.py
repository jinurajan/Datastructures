"""
Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Input: nums = [1,2,3]
Output: 6


thought

1. max product will either the product of last 3 numbers or the product of first two and the last the number (if there are more than 2 negative numbers)
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        p1 = 1
        n = len(nums)
        for i in range(n-1, n-4, -1):
            p1 *= nums[i]
        p2 = 1
        for i in range(2):
            p2 *= nums[i]
        p2 *= nums[n-1]
            
        
        return max(p1, p2)
            