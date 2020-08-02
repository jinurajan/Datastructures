"""
Best Time to Buy and Sell Stock

Solution
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


class SolutionBF(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_profit_i = 0
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                max_profit_i = max(max_profit_i, prices[j] - prices[i])
            print "max_profit by {} is {}".format(prices[i], max_profit_i)
            max_profit = max(max_profit, max_profit_i)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit = max(max_profit, prices[i] - prices[i-1])
        return max_profit


if __name__ == "__main__":
    # print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    # print SolutionBF().maxProfit([7, 1, 5, 3, 6, 4])
    # print Solution().maxProfit([2, 1, 2, 0, 1])
    print SolutionBF().maxProfit([2, 1, 2, 0, 1])
    # print Solution().maxProfit([1, 2, 3, 4, 5])
    # array = [10000 - i for i in range(1000)]