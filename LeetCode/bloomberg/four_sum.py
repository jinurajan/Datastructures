"""
4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def k_sum(nums, target, k):
            result = []
            if not nums:
                return result
            
            avg_value = target // k
            if avg_value < nums[0] or nums[-1] < avg_value:
                return result
            
            if k == 2:
                return two_sum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in k_sum(nums[i+1:], target-nums[i], k-1):
                        result.append([nums[i]] + subset)
            
            return result
            
        
        def two_sum(nums, target):
            result = []
            left = 0
            right = len(nums)-1
            while left < right:
                sum_val = nums[left]+ nums[right]
                if sum_val < target or (left >0 and nums[left] == nums[left-1]):
                    left += 1
                elif sum_val > target or (right < len(nums)-1 and nums[right] == nums[right+1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return result
        
        nums.sort()
        return k_sum(nums, target, 4)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def k_sum(nums, target, k):
            result = []
            if not nums:
                return result
            
            avg_value = target // k
            if avg_value < nums[0] or nums[-1] < avg_value:
                return result
            
            if k == 2:
                return two_sum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in k_sum(nums[i+1:], target-nums[i], k-1):
                        result.append([nums[i]] + subset)
            
            return result
            
        
        def two_sum(nums, target):
            res = []
            s = set()
    
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
    
            return res
        
        nums.sort()
        return k_sum(nums, target, 4)