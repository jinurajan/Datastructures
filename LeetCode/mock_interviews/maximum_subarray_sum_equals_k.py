"""
Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        sum_map = {}
        max_len = 0
        s = 0
        for i in range(n):
            s += nums[i]
            if s == k:
                max_len = max(max_len, i + 1)
            if s - k in sum_map:
                max_len = max(max_len, i - sum_map[s - k])
            if s not in sum_map:
                sum_map[s] = i
        return max_len



class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_dict = {}
        prefix_array = []
        acc = 0
        for idx, n in enumerate(nums):
            acc += n
            prefix_array.append(acc)
            prefix_dict[acc] = idx

        max_len = 0
        for idx, n in enumerate(prefix_array):
            if k == n:
                max_len = max(max_len, idx + 1)
            if k + n in prefix_dict and prefix_dict[k+n] > idx:
                max_len = max(max_len, prefix_dict[k+n]-idx)

        return max_len