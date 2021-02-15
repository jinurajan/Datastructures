"""
Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""
from typing import List


class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                if tuple(nums[:]) not in uniq_sets:
                    output.append(nums[:])
                    uniq_sets.add(tuple(nums[:]))
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        uniq_sets = set()
        output = []
        backtrack()
        return output

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(combination, counter):
            if len(combination) == len(nums):
                res.append(list(combination))
                return
            for num in counter:
                if counter[num] > 0:
                    combination.append(num)
                    counter[num] -= 1
                    backtrack(combination, counter)
                    combination.pop()
                    counter[num] += 1
        res = []
        backtrack([], Counter(nums))
        return res

nums = [1,1,2]
print(Solution().permuteUnique(nums))