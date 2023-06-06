"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Thinking

1. sort the array = O(nlogn) + O(n) iterate and stop if the diff is more than 1
2. sort the array and use sliding window reset start to end if difference is more than 1 and update max_length
3. iterative from 1 and check the string to find it O(-pow(10, 9)) + O(pow(10, 9))

"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        curr_streak = 1
        long_streak = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    curr_streak += 1
                else:
                    long_streak = max(long_streak, curr_streak)
                    curr_streak = 1
        return max(curr_streak, long_streak)
