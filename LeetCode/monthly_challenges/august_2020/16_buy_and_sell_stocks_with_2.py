


class Solution3(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        Tarray = [[0 for i in range(len(prices))] for j in range(2)]
        for i in xrange(2):
            max_diff = 0 - prices[0]
            for j in xrange(len(prices)):
                if j <= 0:
                    profit = 0
                else:
                    profit = Tarray[i][j-1]
                Tarray[i][j] = max(profit, max_diff+prices[j])
                max_diff = max(max_diff, Tarray[i-1][j]-prices[j])
        return Tarray[1][len(prices)-1]



prices = [3,3,5,0,0,3,1,4]
print Solution3().maxProfit(prices)
prices = [1,2,3,4,5]
print Solution3().maxProfit(prices)
prices = [7,6,4,3,1]
print Solution3().maxProfit(prices)
