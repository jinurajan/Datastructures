"""
 Best Time to Buy and Sell Stock

 You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_val = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_stock_val = min(min_stock_val, prices[i])
            max_profit = max(max_profit, prices[i] - min_stock_val)
        return max_profit

