"""
3 Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
from typing import List


class Solution2:
    """ Time Limit Exceeded"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        def backtrack(first, sum, combination, results):
            if len(combination) > 3 or first == n:
                return
            elif len(combination) == 3:
                if sum == 0 and tuple(sorted(combination[:])) not in visited:
                    results.append(combination[:])
                visited.add(tuple(sorted(combination[:])))
                return
            for i in range(first, n):
                combination.append(nums[i])
                backtrack(first+1, sum+nums[i], combination, results)
                combination.pop()
        results = []
        backtrack(0, 0, [], results)
        return sorted(results)

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        start, end = i + 1, len(nums) - 1
        while start < end:
            sum = nums[start] + nums[end] + nums[i]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                res.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1


# nums = [-1,0,1,2,-1,-4]
# print(Solution().threeSum(nums))
# nums = [0]
# print(Solution().threeSum(nums))

nums = [0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14]
print(Solution().threeSum(nums))

