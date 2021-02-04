"""
Longest Harmonious Subsequence
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3]


Input: nums = [1,2,3,4]
Output: 2

Input: nums = [1,1,1,1]
Output: 0

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109

"""
from typing import List
from collections import defaultdict, Counter


class Solution1:
    def findLHS(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        visited = set()
        max_val, count_1, count_2 = 0, 0, 0
        for n in nums:
            num_map[n] += 1
        for key, val in num_map.items():
            if key in visited or (key+1 not in num_map and key-1 not in num_map) :
                continue
            if key+1 in num_map:
                count_1 = num_map[key] + num_map[key+1]
            if key - 1 in num_map:
                count_2 = num_map[key] + num_map[key-1]
            visited.add(key)
            max_val = max(max_val, count_1, count_2)
        return max_val

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = Counter(nums)
        res = 0
        for k, v in d.items():
            if k+1 in d:
                count = d[k+1]+v
                res = max(res, count)
        return res



nums = [1,3,2,2,5,2,3,7]
print(Solution().findLHS(nums))

nums = [1,2,3,4]
print(Solution().findLHS(nums))

nums = [1,1,1,1]
print(Solution().findLHS(nums))








