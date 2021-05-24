"""
Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

"""
from typing import List


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_sq_len = 0
        dp = [[0 if i == 0 or j == 0 else int(matrix[i - 1][j - 1]) for j in range(cols + 1)] for i in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    max_sq_len = max(max_sq_len, dp[i][j])
        return max_sq_len * max_sq_len


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        longest = 0

        dp = [[0 for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0):
                    if matrix[row][col] == "1":
                        dp[row][col] = 1
                elif matrix[row][
                    col] == "1":  # if we have "1" it can potentially ADD "1" to our current sides, else it will be 0
                    dp[row][col] = min(dp[row - 1][col - 1], min(dp[row - 1][col], dp[row][col - 1])) + 1
                longest = max(longest, dp[row][col])

        area = longest ** 2
        return area