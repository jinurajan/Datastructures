"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.


Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp1,dp2 = 0, 0

        for num in nums:
            dp1, dp2 = dp2, max(dp1+num, dp2)
        return dp2

class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def rob_from(index):
            if index >= len(nums):
                return 0
            if index in mem:
                return mem[index]
            mem[index] = max(
                rob_from(index+2) + nums[index],
                rob_from(index+1)
            )
            return mem[index]

        return rob_from(0)