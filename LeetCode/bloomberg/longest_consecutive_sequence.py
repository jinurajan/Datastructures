"""
Longest Consecutive Sequence


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        current_streak = 1
        long_streak = 1
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    long_streak = max(long_streak, current_streak)
                    current_streak = 1
        return max(long_streak, current_streak)
