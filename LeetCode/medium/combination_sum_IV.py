"""
Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Input: nums = [1,2,3], target = 4
Output: 7

"""
from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
        
        return dp[target]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def search(balance):
            if balance == 0:
                return 1
            
            result = 0
            for num in nums:
                if balance -num >= 0:
                    result += search(balance-num)
            
            return result
        
        return search(target)