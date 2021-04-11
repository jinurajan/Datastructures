"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_count = 0
        def dfs(i, j):
            count = 0
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for idx, idy in neighbors:
                x = i+idx
                y = j+idy
                if x < 0 or y < 0 or x > rows-1 or y > cols-1 or matrix[x][y] <= matrix[i][j]:
                    continue
                count = max(count, dfs(x, y))
            return count+1


        for i in range(rows):
            for j in range(cols):
                max_count = max(max_count, dfs(i, j))
        return max_count

from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_count = 0
        cache = defaultdict(lambda: 0)
        def dfs(i, j, cache):
            if cache[(i, j)] > 0:
                return cache[(i, j)]
            count = 0
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for idx, idy in neighbors:
                x = i+idx
                y = j+idy
                if x < 0 or y < 0 or x > rows-1 or y > cols-1 or matrix[x][y] <= matrix[i][j]:
                    continue
                count = max(count, dfs(x, y, cache))
            return count+1
        for i in range(rows):
            for j in range(cols):
                max_count = max(max_count, dfs(i, j, cache))
        return max_count


matrix = [[9,9,4],[6,6,8],[2,1,1]]
import pdb; pdb.set_trace()
print(Solution().longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(Solution().longestIncreasingPath(matrix))
matrix = [[1]]
print(Solution().longestIncreasingPath(matrix))