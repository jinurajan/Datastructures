"""
Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols+1)] for j in range(rows+1)]

        max_len = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
                    max_len = max(max_len, dp[i][j])
        
        return max_len*max_len

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(matrix=matrix))
matrix = [["0","1"],["1","0"]]
print(Solution().maximalSquare(matrix=matrix))