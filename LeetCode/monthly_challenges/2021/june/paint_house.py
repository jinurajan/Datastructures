"""
Paint House

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2

Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""
from typing import List


class Solution1:
    def minCost(self, costs: List[List[int]]) -> int:
        # this is brute force
        n = len(costs)
        def min_cost_recursive(index, curr_color):
            if index == n:
                return 0
            if index >= len(costs):
                return 0
            colors = {0, 1, 2}
            min_cost = float("inf")
            colors.discard(curr_color)
            for color in colors:
                min_cost = min(min_cost, costs[index][color] + min_cost_recursive(index+1, color))
            return min_cost
        return min_cost_recursive(0, -1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[-1 for _ in range(3)] for _ in range(n)]

        def min_cost_recursive(index, curr_color):
            if index >= n:
                return 0
            if dp[index][curr_color] == -1:
                colors = {0, 1, 2}
                min_cost = float("inf")
                colors.discard(curr_color)
                for color in colors:
                    min_cost = min(min_cost, costs[index][color] + min_cost_recursive(index + 1, color))
                dp[index][curr_color] = min_cost
            return dp[index][curr_color]
        return min_cost_recursive(0, -1)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # bottom up
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0] = costs[0]
        for index in range(1, n):
            dp[index][0] = costs[index][0] + min(dp[index-1][1], dp[index-1][2])
            dp[index][1] = costs[index][1] + min(dp[index - 1][0], dp[index - 1][2])
            dp[index][2] = costs[index][2] + min(dp[index - 1][0], dp[index - 1][1])
        return min(dp[-1])




costs = [[17,2,17],[16,16,5],[14,3,19]]
print(Solution().minCost(costs))
costs = [[7,6,2]]
print(Solution().minCost(costs))
costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
print(Solution().minCost(costs))



