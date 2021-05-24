"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need a minimum of two coins {2,3} to make a total of '5'

Given a number array to represent different coin denominations and a total amount ‘T’, we need to find the minimum number of coins needed to make a change for ‘T’. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.
"""
from typing import List
import math

def count_change(denominations, total):
    """
    Time complexity - O( 2 raised N*T)
    Space Complexity - O(N *T) for recursion call
    """
    result = count_change_recursive(denominations, total, 0)
    return -1 if result == math.inf else result


def count_change_recursive(denominations, total, index):
    if total == 0:
        return 0
    n = len(denominations)
    if n == 0 or index == n:
        return math.inf
    c1 = math.inf
    if denominations[index] <= total:
        c1 = count_change_recursive(denominations, total-denominations[index], index)
        if c1 != math.inf:
            c1 += 1
    c2 = count_change_recursive(denominations, total, index+1)
    return min(c1, c2)

def count_change_top_down(denominations, total):
    n = len(denominations)
    if not n or not total:
        return 0
    dp =[[-1 for i in range(total+1)] for j in range(n)]

    def count_change_recursive(total, index):
        if total == 0:
            return 0
        if index >= n:
            return math.inf

        if dp[index][total] == -1:
            c1 = math.inf
            if denominations[index] <= total:
                c1 = count_change_recursive(total - denominations[index], index)
                if c1 != math.inf:
                    c1 += 1
            c2 = count_change_recursive(total, index + 1)
            dp[index][total] = min(c1, c2)
        return dp[index][total]
    res = count_change_recursive(total, 0)
    return -1 if res == math.inf else res



def count_change_bottom_up(denominations, total):
    """
    Time: O(N *C)
    Space:  O(N *C)
    """
    n = len(denominations)
    if not n or not total:
        return 0
    dp = [[math.inf for i in range(total+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(1, total+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= denominations[i]:
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-denominations[i]])
    return -1 if dp[n - 1][total] == math.inf else dp[n - 1][total]


def coinChange(coins: List[int], amount: int) -> int:
    if not coins or not amount:
        return 0
    n = len(coins)
    dp = [float("inf") for i in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    return dp[amount] if dp[amount] != float("inf") else -1



print(count_change([1, 2, 3], 5))
print(count_change([1, 2, 3], 11))
print(count_change([1, 2, 3], 7))
print(count_change([3, 5], 7))


print(count_change_top_down([1, 2, 3], 5))
print(count_change_top_down([1, 2, 3], 11))
print(count_change_top_down([1, 2, 3], 7))
print(count_change_top_down([3, 5], 7))


print(count_change_bottom_up([1, 2, 3], 5))
print(count_change_bottom_up([1, 2, 3], 11))
print(count_change_bottom_up([1, 2, 3], 7))
print(count_change_bottom_up([3, 5], 7))


print(coinChange([1, 2, 3], 5))
print(coinChange([1, 2, 3], 11))
print(coinChange([1, 2, 3], 7))
print(coinChange([3, 5], 7))