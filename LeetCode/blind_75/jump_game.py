"""
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_idx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if target_idx <= i+nums[i]:
                target_idx = i
        
        if target_idx == 0:
            return True
        return False