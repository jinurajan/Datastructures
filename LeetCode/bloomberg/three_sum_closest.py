"""
3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float("inf")
        for i in range(n):
            l = i+1
            r = n-1
            while l< r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(target-sum) < abs(diff):
                    diff = target - sum
                if sum > target:
                    r -= 1
                else:
                    l += 1
                if diff == 0:
                    break
        return target-diff