"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
"""
from typing import List


class Solution:
    def two_sum(self, nums, right, target):
        left = 0
        results = []
        while left<right:
            s = nums[left] + nums[right]
            if s == target:
                results.append([nums[left], nums[right]])
            if s < target:
                left += 1
            else:
                right -= 1
        return results
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        visited = set()
        n = len(nums)
        for i in range(n-1, 1, -1):
            two_sums = self.two_sum(nums, i-1, 0-nums[i])
            for two_sum in two_sums:
                r = two_sum + [nums[i]]
                if tuple(r) not in visited:
                    results.append(r)
                    visited.add(tuple(r))
        return results
