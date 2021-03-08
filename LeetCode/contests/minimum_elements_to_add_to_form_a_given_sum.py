"""
You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2
Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
Example 2:

Input: nums = [1,-10,9,1], limit = 100, goal = 0
Output: 1

Constraints:

1 <= nums.length <= 105
1 <= limit <= 106
-limit <= nums[i] <= limit
-109 <= goal <= 109

"""
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        curr_sum = sum(nums)
        target = goal - curr_sum
        if target < 0:
            target = -target
        weights = [i for i in range(1, limit + 1)]
        T = [float("inf") if i not in weights else 1 for i in range(target + 1)]
        for i in range(1, target + 1):
            for w in weights:
                if i - w >= 0:
                    T[i] = min(T[i], T[i - w] + 1)
        return T[-1]

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        target = abs(sum(nums) - goal)
        limit = abs(limit)
        count, r = divmod(target, limit)
        if r:
            count += 1
        return count

