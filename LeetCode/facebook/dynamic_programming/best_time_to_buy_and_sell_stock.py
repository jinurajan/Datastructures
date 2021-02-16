"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > 0:
                    profit = max(profit, prices[j] - prices[i])
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_val)
            min_val = min(min_val, prices[i])
        return max_profit

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))