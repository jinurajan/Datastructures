"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(rows):
            for j in range(cols):
                if(i,j) == (0,0):
                    continue
                is_valid = lambda i,j: 0<=i<rows and 0<=j<cols
                if is_valid(i-1,j) and is_valid(i,j-1):
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                elif is_valid(i-1, j):
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
        return dp[rows-1][cols-1]
            




