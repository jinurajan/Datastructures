"""
Closest Subsequence Sum
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.



Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7


Constraints:

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109
"""
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        st1 = {0}
        st2 = {0}
        for i in range(n // 2):
            st1 |= {x + nums[i] for x in st1}
        print(st1)
        for i in range(n // 2, n):
            st2 |= {x + nums[i] for x in st2}
        print(st2)
        st1, st2 = sorted(st1), sorted(st2)
        n1, n2 = len(st1), len(st2)
        i, j = 0, n2 - 1
        res = abs(goal)
        while i <= n1 - 1 and j >= 0:
            if st1[i] + st2[j] - goal > 0:
                res = min(res, st1[i] + st2[j] - goal)
                j -= 1
            elif st1[i] + st2[j] - goal < 0:
                res = min(res, goal - st1[i] - st2[j])
                i += 1
            else:
                return 0
        return res

nums = [7,-9,15,-2]
goal = -5
print(Solution().minAbsDifference(nums, goal))
