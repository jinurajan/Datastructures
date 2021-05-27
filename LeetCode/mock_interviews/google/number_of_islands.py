"""
Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and grid[x][y] == '1':
                grid[x][y] = '-1'
                for dx, dy in neighbors:
                    dfs(x + dx, y + dy)
            return

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands

