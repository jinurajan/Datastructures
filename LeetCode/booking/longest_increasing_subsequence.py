"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # intelligently create subsequence
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)