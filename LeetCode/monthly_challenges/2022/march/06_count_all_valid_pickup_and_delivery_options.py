"""
Count All Valid Pickup and Delivery Options

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500

"""
from functools import cache


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for unpicked in range(n+1):
            for undelivered in range(n+1):
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked-1][undelivered]
                dp[unpicked][undelivered] %= MOD

                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered-unpicked) * dp[unpicked][undelivered-1]
                dp[unpicked][undelivered] %= MOD
        return dp[n][n]

class Solution1:
    def countOrders(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        
        @cache
        def total_ways(unpicked, undelivered):
            if not unpicked and not undelivered:
                # done with all options
                return 1
            if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
                return 0
            result = unpicked * total_ways(unpicked-1, undelivered)
            result %= MOD
            
            result += (undelivered - unpicked)*total_ways(unpicked, undelivered - 1)
            result %= MOD
            return result
        
        return total_ways(n,n)

class Solution2:
    def countOrders(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[-1 for i in range(n+1)] for j in range(n+1)]

        def total_ways(unpicked, undelivered):
            if not unpicked and not undelivered:
                # done with all options
                return 1
            if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
                return 0
            if dp[unpicked][undelivered] != -1:
                return dp[unpicked][undelivered]
            
            p1 = unpicked * total_ways(unpicked-1, undelivered)
            p1 %= MOD
            
            p1 += (undelivered - unpicked)*total_ways(unpicked, undelivered - 1)
            p1 %= MOD
            dp[unpicked][undelivered] = p1
            return dp[unpicked][undelivered]
        total_ways(n,n)
        return dp[n][n]


n = 1
print(Solution().countOrders(n=n))
n = 2
print(Solution().countOrders(n=n))
n = 3
print(Solution().countOrders(n=n))



        