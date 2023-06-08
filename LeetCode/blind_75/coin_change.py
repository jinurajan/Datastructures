"""
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin


Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1


Thoughts

1. dp -> build all 

dp[i] = 1 if i == x
else min(dp[i-x] for x in coins) + 1

edge cases
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = 1 if i == coins value
        # else min(dp[i-x] for x in coins)
        # if amount is 0 return 0
        if not coins or not amount:
            return 0
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1