"""
House Robber


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  return 0
        if n == 1:  return nums[0]
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1+num, dp2)
        return dp2



class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  return 0
        if n == 1:  return nums[0]
        T = [0 for i in range(n)]
        T[0] = nums[0]
        T[1] = nums[1] if nums[0] < nums[1] else nums[0]
        for i in range(2, n):
            T[i] = max(T[i-2]+nums[i], T[i-1])
        print(T)
        return T[-1]
            


# print(Solution().rob([1,2,3,1]))
# print(Solution().rob([2,7,9,3,1]))
# print(Solution().rob([2,1, 1, 2]))
# print(Solution().rob([6,3,10,8,2,10,3,5,10,5,3])) #39

print("*****")
print(Solution1().rob([1,2,3,1]))
print(Solution1().rob([2,7,9,3,1]))
print(Solution1().rob([2,1, 1, 2]))
print(Solution1().rob([6,3,10,8,2,10,3,5,10,5,3]))
