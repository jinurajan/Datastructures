"""
You're given an integer total and a list of integers called coins. The variable coins hold a list of coin denominations, and total is the total amount of money.

You have to find the minimum number of coins that can make up the total amount by using any combination of the coins. If the amount can't be made up, return -1. If the total amount is 0, return 0.
"""




def coin_change(coins, total):
    # create an array for the total 
    # bottom up
    dp = [float("inf") for i in range(total+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total+1):
            dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[-1] if dp[-1] != float("inf") else -1

