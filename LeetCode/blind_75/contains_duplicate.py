"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash map
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        return False