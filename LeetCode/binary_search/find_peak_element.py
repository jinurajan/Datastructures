"""
Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.

"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        else:
            l, r = 0, n-1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    r = mid
                else:
                    l = mid + 1
            return l


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        def binary_search(nums, l, r):
            if l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid+1]:
                    return binary_search(nums, l, mid)
                return binary_search(nums, mid + 1, r)
            return l
        return binary_search(nums, 0, n-1)

                
print(Solution().findPeakElement(nums=[1,2,1,3,5,6,4]))
print(Solution1().findPeakElement(nums=[1,2,1,3,5,6,4]))