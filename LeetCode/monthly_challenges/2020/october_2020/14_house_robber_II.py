"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n <= 3:
            return max(nums)
        def helper(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp1, dp2 = dp2, max(dp1+num, dp2)
            return dp2
        return max(nums[0]+ helper(nums[2:-1]), helper(nums[1:]))

import pdb; pdb.set_trace()
print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2, 1]))
print(Solution().rob([1,2,1,1]))
