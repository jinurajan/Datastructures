"""
Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
import random

def quick_sort(nums):
        
        if len(nums) <= 1:
            return nums
        
        lo = []
        hi = []
        eq = []
        pivot = random.choice(nums)
        
        for i in nums:
            if i == pivot:
                eq.append(i)
            elif (int(i + pivot)) > (int(pivot + i)):
                hi.append(i)
            else: 
                lo.append(i)
        
        return quick_sort(hi) + eq + quick_sort(lo)



class Solution1(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = quick_sort([str(n) for n in nums])
        return '0' if nums[0] == '0' else "".join(nums)

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        res = sorted(nums, cmp=lambda a, b:cmp(b+a, a+b))
        return '0' if res[0] == '0' else "".join(nums)


        
print Solution().largestNumber([3,30,34,5,9])
print Solution1().largestNumber([3,30,34,5,9])