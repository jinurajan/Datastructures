"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water


m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


Thoughts

1. what should be considered as the value outside the matrix ? 0 ?
2. island when all neighbours are 0 for a connected land -> find the number of connected 1's
3. can use some value for visited value for values with 1 -> may be replace it with X ?

dfs ? -> try all neighbours if the stack becomes empty increase the count

idea

1. find all x, y with value as 1

start dfs with each value from stack and keep adding if the neigbbour is 1 add the col as visited while traverse -> when stack becomes empty increase count


space complexity min(M, N)

time complexity O(M*N)
"""

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs recursive
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        neighbors = [(0,1), (1, 0), (-1, 0), (0, -1)]
        def valid(x, y):
            if 0 <= x <= rows-1 and 0 <= y <= cols-1:
                return True
            return False

        def dfs(x, y):
            if valid(x, y) and grid[x][y] == '1':
                grid[x][y] = 'X'
                for dx, dy in neighbors:
                    dfs(x+dx, y+dy)
            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands += 1
        return islands
    


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        q = deque([])

        def valid(x, y):
            if 0 <= x <= rows-1 and 0 <= y <= cols-1:
                return True
            return False

        neighbors = [(0,1), (1, 0), (-1, 0), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    q.append((i, j))
                    grid[i][j] = 'X'
                    while q:
                        x, y = q.pop()
                        for dx, dy in neighbors:
                            if not valid(x+dx, y+dy):
                                continue
                            if grid[x+dx][y+dy] == '1':
                                grid[x+dx][y+dy] = 'X'
                                q.append((x+dx, y+dy))
        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        q = deque([])

        def valid(x, y):
            if 0 <= x <= rows-1 and 0 <= y <= cols-1:
                return True
            return False

        neighbors = [(0,1), (1, 0), (-1, 0), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    q.append((i, j))
                    grid[i][j] = 'X'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in neighbors:
                            if not valid(x+dx, y+dy):
                                continue
                            if grid[x+dx][y+dy] == '1':
                                grid[x+dx][y+dy] = 'X'
                                q.append((x+dx, y+dy))
        return islands





grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().numIslands(grid))

