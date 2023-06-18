"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf") for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n+1):
            dp[i] = min(cost[i-2]+dp[i-2], cost[i-1]+dp[i-1])
        
        return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_1, step_2 = 0, 0
        n = len(cost)
        for i in range(2, n+1):
            step_1, step_2 = min(step_1+cost[i-1], step_2+cost[i-2]), step_1
        
        return step_1