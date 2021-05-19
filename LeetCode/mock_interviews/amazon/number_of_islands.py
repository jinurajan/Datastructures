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
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


"""
from typing import List


from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def backtrack(x, y):
            if 0 <= x <= rows - 1 and 0 <= y <= cols - 1:
                if grid[x][y] != '1':
                    return
                grid[x][y] = '-1'
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in neighbors:
                    backtrack(x + dx, y + dy)
            return

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    backtrack(i, j)
                    islands += 1
        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque([])
        islands = 0
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    q.append((i, j))
                    grid[i][j] = 1
                    while q:
                        x, y = q.pop()
                        for dx, dy in neighbors:
                            if not (0 <= x + dx <= rows - 1 and 0 <= y + dy <= cols - 1):
                                continue
                            if grid[x + dx][y + dy] == '1':
                                grid[x + dx][y + dy] = '-1'
                                q.append((x + dx, y + dy))
        return islands

