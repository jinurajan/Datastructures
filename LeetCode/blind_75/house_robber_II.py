"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.


Thoughts
1. DP extension of previous one 
if array is [1,2,3,4,5, 6]

result would be [1,2,3,4,5] or [2,3,4,5,6] # include and exclude either last / first value in the list

"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))
    

    def rob_simple(self, nums: List[int]) -> int:
        dp1 = 0
        dp2 = 0

        for num in nums:
            dp1, dp2 = dp2, max(dp1+num, dp2)
        return dp2