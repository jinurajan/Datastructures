"""
Find All Numbers Disappeared in an Array

Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        res = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                res.append((i))
        return res


nums = [4,3,2,7,8,2,3,1]
print(Solution1().findDisappearedNumbers(nums))

