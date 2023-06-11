"""
Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Input: nums = [1,3,5,6], target = 5
Output: 2


Input: nums = [1,3,5,6], target = 2
Output: 1
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def bs(left, right, target):
            if left > right:
                return left
            mid = (left + right )// 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return bs(mid+1, right, target)
            else:
                return bs(left, mid-1, target)
        return bs(0, len(nums)-1, target)