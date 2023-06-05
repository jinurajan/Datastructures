"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, n in enumerate(nums):
            if target-n in hash_map:
                return [hash_map[target-n], idx]
            hash_map[n] = idx
