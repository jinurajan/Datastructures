"""
Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [0] * n
        R = [0] * n
        res = [0] * n
        L[0], R[-1] = 1, 1
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            R[j] = R[j+1] * nums[j+1]
        for i in range(n):
            res[i] = L[i] * R[i]
        return res