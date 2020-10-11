"""

Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List

class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i] == 1:
                start = i
                break
        end = start
        res = 0
        while end <= n:
            if end == n:
                res = max(res, end-start)
                break  
            if nums[end] != 1:
                # reached 0
                res = max(res, end-start)
                start = end + 1
            end = end + 1
        return res

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        running_sum = 0
        for num in nums:
            if num:
                running_sum += num
            else:
                res = max(res, running_sum)
                running_sum = 0
        return max(res, running_sum)

import pdb; pdb.set_trace()
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(Solution().findMaxConsecutiveOnes([1,1]))
print(Solution().findMaxConsecutiveOnes([1]))
