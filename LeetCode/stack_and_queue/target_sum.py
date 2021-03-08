"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """ TLE """
        n = len(nums)
        def dfs(combination, next_digit, sum_val, S):
            nonlocal count
            if not next_digit:
                if sum_val == S:
                    count += 1
                return
            else:
                combination.append(f'+{next_digit[0]}')
                dfs(combination, next_digit[1:], sum_val + next_digit[0], S)
                combination.pop()
                combination.append(f'-{next_digit[0]}')
                dfs(combination, next_digit[1:], sum_val - next_digit[0], S)
        count = 0
        dfs([], nums, 0, S)
        return count


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        mem = [[0 for i in range(2001)] for j in range(2001)]

        def calculate(nums, i, curr_sum, S):
            if i == len(nums):
                if curr_sum == S:
                    return 1
                else:
                    return 0
            else:
                if mem[i][curr_sum + 1000] != 0:
                    return mem[i][curr_sum + 1000]
                add = calculate(nums, i + 1, curr_sum + nums[i], S)
                substract = calculate(nums, i + 1, curr_sum - nums[i], S)
                mem[i][curr_sum + 1000] = add + substract
                return mem[i][curr_sum + 1000]

        return calculate(nums, 0, 0, S)


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """ TLE"""
        dp = [[0 for i in range(2001)] for j in range(2001)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for s in range(-1000, 1001):
                if dp[i - 1][s + 1000] > 0:
                    dp[i][s + nums[i] + 1000] += dp[i - 1][s + 1000]
                    dp[i][s - nums[i] + 1000] += dp[i - 1][s + 1000]
        if S > 1000:
            return 0
        else:
            return dp[len(nums) - 1][S + 1000]


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [0 for i in range(2001)]
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            next = [0 for i in range(2001)]
            for s in range(-1000, 1001):
                if dp[s + 1000] > 0:
                    next[s + nums[i] + 1000] += dp[s + 1000]
                    next[s - nums[i] + 1000] += dp[s + 1000]
            dp = next
        if S > 1000:
            return 0
        else:
            return dp[S + 1000]


nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))