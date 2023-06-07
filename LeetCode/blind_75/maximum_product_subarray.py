"""
Maximum Product Subarray

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        n = len(nums)
        result = max_so_far
        for i in range(1, n):
            curr = nums[i]
            tmp_max = max(curr, min_so_far*curr, max_so_far*curr)
            min_so_far = min(curr, min_so_far*curr, max_so_far*curr)
            max_so_far = tmp_max
            result = max(result, max_so_far)
        return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -math.inf
        n = len(nums)
        for i in range(n):
            p = nums[i]
            for j in range(i+1, n):
                p *= nums[j]
                max_product = max(p, max_product)
        return max_product
