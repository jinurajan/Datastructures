"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = set()
        def backtrack(idx, permutation):
            if len(permutation) == n:
                result.append(permutation[:])
                return
            for i in range(n):
                if i in visited:
                    continue
                permutation.append(nums[i])
                visited.add(i)
                backtrack(i, permutation)
                visited.remove(i)
                permutation.pop()
        backtrack(0, [])
        return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(idx):
            if idx == n:
                result.append(nums[:])
            else:
                for i in range(idx, n):
                    nums[i], nums[idx] = nums[idx], nums[i]
                    backtrack(idx+1)
                    nums[i], nums[idx] = nums[idx], nums[i]
        backtrack(0)
        return result