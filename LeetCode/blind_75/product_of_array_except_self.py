"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


thoughts
1. can it have 0 ? yes
2. max value will fit in 32 bit integer
3. O(n)
4. prefix product ??
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using same array for computing left and right product 
        n = len(nums)
        result = [0] * n
        result[0] = 1
        for i in range(1, n):
            result[i] = nums[i-1] * result[i-1]
        
        R = 1
        for i in reversed(range(n)):
            result[i] = result[i] * R
            R *= nums[i]
        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using left and right side product and using it to compute the product except self
        n = len(nums)
        L = [0] * n
        R = [0] * n
        result = [0] *n
        L[0] = R[-1] = 1
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1]  *nums[i+1]
        for i in range(n):
            result[i] = L[i]*R[i]
        return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        zero_indices = set()
        for idx, num in enumerate(nums):
            if num == 0:
                zero_indices.add(idx)
                continue
            max_product *= num
        
        result = []
        for idx, num in enumerate(nums):
            if idx in zero_indices:
                if len(zero_indices) > 1:
                    result.append(0)
                else:
                    result.append(max_product)
            else:
                if zero_indices:
                    result.append(0)
                else:
                    result.append(max_product // num)
        return result




