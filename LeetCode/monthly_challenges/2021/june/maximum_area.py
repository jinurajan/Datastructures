"""
Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def is_valid(x, y):
            return 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and grid[x][y]

        def dfs(x, y, area):
            nonlocal max_area
            if not is_valid(x, y):
                return 0
            grid[x][y] = 0
            count = 1
            for dx, dy in neighbors:
                count += dfs(x + dx, y + dy, area + 1)
            return count
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area =  dfs(i, j, 0)
                    max_area = max(max_area, area)
        return 0 if max_area == float("-inf") else max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))