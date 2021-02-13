"""
Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid[0] or not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])

        def get_islands(i, j, path):
            if i < 0 or j < 0 or i > rows-1 or j > columns-1:
                return
            if  (i,j) in visited or grid[i][j] == '0':
                return
            visited.add((i, j))
            path.append((i, j))
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in neighbors:
                get_islands(i+x, j+y, path)
        visited = set()
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    path = []
                    get_islands(i, j, path)
                    if path:
                        count += 1
        return count


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# print(Solution().numIslands(grid) == 1)

grid = grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
import pdb; pdb.set_trace()
print(Solution().numIslands(grid) == 3)