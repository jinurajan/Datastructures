"""
Allocate Mailboxes

Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5

Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Input: houses = [7,4,6,1], k = 1
Output: 8

Input: houses = [3,6,14,10], k = 4
Output: 0

"""


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        N = len(houses)
        houses.sort()
        dp = {}

        def helper(n, k):
            if (n, k) in dp: return dp[(n, k)]
            if n == k: return 0
            if k == 1:
                dp[(n, k)] = sum(houses[(n + 1) // 2:n]) - sum(houses[:n // 2])
                return dp[(n, k)]

            res = helper(n - 1, k - 1)
            f = 0
            for j in range(2, n + 2 - k):
                f += houses[n - (j + 1) // 2] - houses[n - j]
                if f > res: break
                res = min(res, f + helper(n - j, k - 1))
            dp[(n, k)] = res
            return res

        return helper(N, k)



class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()  # ascending order
        n = len(houses)
        mdist = [[0] * n for _ in range(n)]  # mdist[i][j] median distance of houses[i:j+1]
        for i in range(n):
            for j in range(i + 1, n):
                mdist[i][j] = mdist[i][j - 1] + houses[j] - houses[i + j >> 1]

        @cache
        def fn(n, k):
            """Return min distance of allocating k mailboxes to n houses."""
            if n <= k: return 0  # one mailbox for each house
            if k == 1: return mdist[0][n - 1]
            ans = inf
            for nn in range(k - 1, n):
                ans = min(ans, fn(nn, k - 1) + mdist[nn][n - 1])
            return ans

        return fn(n, k)

