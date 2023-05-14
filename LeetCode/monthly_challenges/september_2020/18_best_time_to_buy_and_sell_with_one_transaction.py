"""
Best Time to Buy and Sell Stock (Easy)
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        result = [0]*n
        min_stock_price = prices[0]
        for i in range(1, n):
            result[i] = max(result[i-1], prices[i] - min_stock_price)
            if min_stock_price > prices[i]:
                min_stock_price = prices[i]
        return result[-1]



class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        max_profit = 0
        min_stock_price = prices[0]
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_stock_price)
            if min_stock_price > prices[i]:
                min_stock_price = prices[i]
        return max_profit


print Solution().maxProfit([7,1,5,3,6,4])
print Solution().maxProfit([7,6,4,3,1])

print Solution1().maxProfit([7,1,5,3,6,4])
print Solution1().maxProfit([7,6,4,3,1])
