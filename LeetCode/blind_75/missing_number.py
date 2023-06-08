"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n * (n+1) // 2

        return exp_sum - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in num_set:
                return num
    

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
