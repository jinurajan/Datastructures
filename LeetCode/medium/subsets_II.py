"""
90. Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        uniq_sets = set()

        def search(k):
            if k == n:
                r = sorted(subset[:])
                if tuple(r) not in uniq_sets:
                    result.append(r)
                    uniq_sets.add(tuple(r))
                return
            subset.append(nums[k])
            search(k + 1)
            subset.pop()
            search(k + 1)

        result = []
        subset = []
        search(0)
        return result
