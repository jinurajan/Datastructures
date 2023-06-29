"""
Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



"""
from typing import List


class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        Tarray = [[0 for i in range(len(prices))] for j in range(2)]
        for i in range(2):
            max_diff = 0 - prices[0]
            for j in range(len(prices)):
                if j <= 0:
                    profit = 0
                else:
                    profit = Tarray[i][j-1]
                Tarray[i][j] = max(profit, max_diff+prices[j])
                max_diff = max(max_diff, Tarray[i-1][j]-prices[j])
        return Tarray[1][len(prices)-1]
    


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left_min = prices[0]
        right_max = prices[-1]

        n= len(prices)
        left_profits = [0] * n

        right_profits = [0] * (n+1)

        for i in range(1, n):
            left_profits[i] = max(left_profits[i-1], prices[i]-left_min)

            left_min = min(left_min, prices[i])

            r = n -1-i
            right_profits[r] = max(right_profits[r+1], right_max-prices[r])

            right_max = max(right_max, prices[r])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])
        
        return max_profit



class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price-t1_cost)

            t2_cost = min(t2_cost, price-t1_profit)
            t2_profit = max(t2_profit, price-t2_cost)
        
        return t2_profit


prices = [3,3,5,0,0,3,1,4]
print Solution3().maxProfit(prices)
prices = [1,2,3,4,5]
print Solution3().maxProfit(prices)
prices = [7,6,4,3,1]
print Solution3().maxProfit(prices)
