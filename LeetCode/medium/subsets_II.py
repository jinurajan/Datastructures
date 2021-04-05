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


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for mask in range(2 ** n):
            subset = []
            i = 0
            while mask:
                if mask & 1:
                    subset.append(nums[i])
                i += 1
                mask >>= 1
            result.add(tuple(subset))
        return list(result)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        visited = set()
        results = []
        subset = []

        def backtrack(index):
            if index == n:
                if tuple(subset) not in visited:
                    results.append(subset[:])
                    visited.add(tuple(subset))
                return
            backtrack(index + 1)
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

        backtrack(0)
        return results


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        n = len(nums)

        def backtrack(index, subset):
            if index == n:
                results.append(subset[:])
                return
            count = 1
            j = index + 1
            while j <= n - 1 and nums[index] == nums[j]:
                j += 1
                count += 1
            # excluding duplicate values
            backtrack(index + count, subset)
            # including duplicate values in the subset
            for c in range(1, count + 1):
                subset.append(nums[index])
                backtrack(index + count, subset)
            for c in range(1, count + 1):
                subset.pop()
        backtrack(0, [])
        return results


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]

        prev = None

        for i in range(len(nums)):

            if i and nums[i] == nums[i - 1]:
                copy = prev
            else:
                copy = subsets[:]

            level = []
            for element in copy:
                temp = element + [nums[i]]
                level.append(temp)
                subsets.append(temp)
            prev = level
            print(subsets, prev)
            print("************")

        return subsets


print(Solution().subsetsWithDup([2,1,2]))
