"""
Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

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
        if not grid or not grid[0]:
            return
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        q = deque()
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    q.append((i, j))
                    grid[i][j] = 1
                    while q:
                        x, y = q.pop()
                        for idx, idy in neighbors:
                            if x + idx < 0 or x + idx >= rows or y + idy < 0 or y + idy >= cols:
                                continue
                            if grid[x + idx][y + idy] == '1':
                                grid[x + idx][y + idy] = '-1'
                                q.append((x + idx, y + idy))
        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return
        rows = len(grid)
        cols = len(grid[0])

        def get_islands(i, j, path):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if (i, j) in visited or grid[i][j] == '0':
                return
            visited.add((i, j))
            path.append((i, j))
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for idx, idy in neighbors:
                get_islands(i + idx, j + idy, path)

        visited = set()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    path = []
                    get_islands(i, j, path)
                    if path:
                        count += 1
        return count


from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y, visited):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if (x, y) in visited or grid[x][y] == "0":
                return
            visited.add((x, y))
            neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for idx, idy in neighbors:
                dfs(x + idx, y + idy, visited)

        islands = 0
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    print(visited)
                    islands += 1
        return islands

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(Solution().numIslands(grid))