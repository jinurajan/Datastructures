"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return nums[0]
        nums = sorted(nums)
        idx = 0
        while idx < n-1:
            if nums[idx] != nums[idx+1]:
                return nums[idx]
            idx += 2
        return nums[idx]



class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
            print(a)
        return a

print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))

