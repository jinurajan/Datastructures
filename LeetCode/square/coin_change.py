"""
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [float("inf") for i in range(amount+1)]
        coins = set(coins)
        for i in range(amount+1):
            if i in coins:
                dp[i] = 1
        
        for coin in coins:
            for i in range(1, amount+1):
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1