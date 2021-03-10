"""
Matrix Block Sum
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0 for i in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
        result = [[0] * (cols) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                topleft_x, topleft_y = max(0, i - K), max(0, j - K)
                bottomright_x, bottomright_y = min(rows, i + K + 1), min(cols, j + K + 1)
                bottomleft_x, bottomleft_y = bottomright_x, topleft_y
                topright_x, topright_y = topleft_x, bottomright_y
                result[i][j] = dp[bottomright_x][bottomright_y] - dp[bottomleft_x][bottomleft_y] - dp[topright_x][
                    topright_y] + dp[topleft_x][topleft_y]
        return result

