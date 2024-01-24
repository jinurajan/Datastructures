"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
"""
from typing import List


class Solution1:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        visited = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if tuple(sorted((nums[i], nums[j], nums[k]))) not in visited:
                            results.append([nums[i], nums[j], nums[k]])
                            visited.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return results

class Solution2:
    def two_sum(self, nums, right, target):
        left = 0
        results = []
        while left<right:
            s = nums[left] + nums[right]
            if s == target:
                results.append([nums[left], nums[right]])
            if s < target:
                left += 1
            else:
                right -= 1
        return results
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        visited = set()
        n = len(nums)
        for i in range(n-1, 1, -1):
            two_sums = self.two_sum(nums, i-1, 0-nums[i])
            for two_sum in two_sums:
                r = two_sum + [nums[i]]
                if tuple(r) not in visited:
                    results.append(r)
                    visited.add(tuple(r))
        return results


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, results)
        return results
    
    def twoSum(self, nums: List[int], i: int, results: List[List[int]]):
        visited = set()
        j = i + 1
        while j < len(nums):
            compliment = -(nums[i]+nums[j])
            if compliment in visited:
                results.append([nums[i], nums[j], compliment])
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            visited.add(nums[j])
            j += 1


class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        dups = set()
        visited = {}
        for i, val_1 in enumerate(nums):
            if val_1 not in dups:
                dups.add(val_1)
                for j, val_2 in enumerate(nums[i+1:]):
                    compliment = -(val_1+val_2)
                    if compliment in visited and visited[compliment] == i:
                        result.append(sorted([val_1, val_2, compliment]))
                    visited[val_2] = i
        return result


nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]
print(Solution1().threeSum(nums=nums))
print(Solution2().threeSum(nums=nums))
print(Solution3().threeSum(nums=nums))
print(Solution4().threeSum(nums=nums))