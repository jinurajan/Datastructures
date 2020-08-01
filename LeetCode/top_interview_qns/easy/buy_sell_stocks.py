"""
Best Time to Buy and Sell Stock II

Solution
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

Solution Idea
i = transactions for trading
j = number of days / length of array

T[i][j] = maximum (T[i][j-1], price[j] - price[m] + max(T[i-1][m]) where from m = 0 to j-1)

example = T[1][1] = max (T[1][0], max(price[j] - price[0] +T[0][1], price[j] - price[1] +T[0][2], price[j] - price[2] +T[0][3]))
        T[2][1] = max (T[2][0], max(T[1][0], T[1][1], T[1,2]))


optimized into the below since price[j] is constant in the loop by finding max diff
"""
from math import ceil


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Tarray = [[0 for i in range(len(prices))] for j in range(len(prices))]
        max_profit = 0
        for i in range(len(prices)):
            max_diff = 0-prices[0]
            for k in range(len(prices)):
                Tarray[i][k] = max(prices[k]+max_diff, Tarray[i][k-1])
                max_diff = max(max_diff, Tarray[i-1][k]-prices[k])
            max_profit = max(max_profit, Tarray[i][k])
        return max_profit


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # no of transactions will at max len(prices)
        Tarray = [[0 for i in range(len(prices))] for j in range(len(prices))]
        max_profit = 0
        for i in range(len(prices)):
            # import pdb; pdb.set_trace()
            for k in range(len(prices)):
                if i == 0 or k == 0:
                    # cannot make profit without transaction
                    Tarray[i][k] = 0
                    continue
                max_value = 0
                for m in range(k):
                    max_value = max(max_value, prices[k]-prices[m]+Tarray[i-1][m])
                Tarray[i][k] = max(Tarray[i][k - 1], max_value)
            max_profit = max(max_profit, Tarray[i][j])
        print Tarray
        return max_profit


class SolutionBF(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_sum = 0
        for i in xrange(len(prices)):
            for j in xrange(i, len(prices)):
                if prices[j]-prices[i] > max_profit:
                    max_profit = prices[j]-prices[i]
            print "max_profit by using {} is {}".format(
                prices[i], max_profit)
            max_sum += max_profit if max_profit > 0 else 0
        return max_profit


class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        T = int(ceil(len(prices)//2))
        Tarray = [[0 for i in range(len(prices))] for j in range(T)]
        for i in xrange(T):
            max_diff = 0 - prices[0]
            for j in xrange(len(prices)):
                if j <= 0:
                    profit = 0
                else:
                    profit = Tarray[i][j-1]
                Tarray[i][j] = max(profit, max_diff+prices[j])
                max_diff = max(max_diff, Tarray[i-1][j]-prices[j])
            if max_diff == -1:
                # peek at the first element
                return 0
        return Tarray[T-1][len(prices)-1]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


if __name__ == "__main__":
    # print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    # print Solution().maxProfit([1, 2, 3, 4, 5])
    # array = [10000 - i for i in range(1000)]
    # print array
    # print Solution().maxProfit(array)
    # print SolutionBF().maxProfit([1, 2, 3, 4, 5])
    # print SolutionBF().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    # print Solution().maxProfit([1,2,3,4,5])
    # array = [100000 - i for i in xrange(100000)]
    # print array
    # print Solution().maxProfit(array)
