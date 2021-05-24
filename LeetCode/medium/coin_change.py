"""
Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""
from typing import List

from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        C = sorted(coins, reverse=True)
        N = [ amount//c for c in C ]
        A = 1 << amount
        M = (A<<1)-1
        v = 1
        n = 1
        while True:
            while N and n > N[0]:
                del N[0]
                del C[0]
            w = 0
            for c in C:
                w |= (v << c) & M
            if w & A:
                return n
            if w & (A-1) == 0:
                return -1
            v = w
            n += 1


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1


coins = [1,2,5]
amount = 11
print(Solution1().coinChange(coins, amount))
print(Solution().coinChange(coins, amount))
