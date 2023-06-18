"""
Coloring A Border


You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares are called adjacent if they are next to each other in any of the 4 directions.

Two squares belong to the same connected component if they have the same color and they are adjacent.

The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.

"""
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        def cal(i, j, c):
            if not (0<=i<rows and 0<=j<cols):
                return 1
            return grid[i][j] != c and grid[i][j] != -1
        
        def dfs(i, j):
            if not (0 <= i < rows and 0 <=j<cols):
                return
            visited.add((i,j))
            c = grid[i][j]
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i = i + di
                new_j = j + dj
                if 0 <=new_i<rows and 0<=new_j<cols and grid[new_i][new_j] == c and (new_i, new_j) not in visited:
                    dfs(new_i, new_j)
            
            if cal(i-1, j, c) or cal(i+1, j, c) or cal(i,j+1, c) or cal(i, j-1, c):
                grid[i][j] = -1

        visited = set()
        dfs(row, col)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == -1:
                    grid[i][j] = color
        return grid


grid = [[1,1],[1,2]]
row = 0
col = 0
color = 3
print(Solution().colorBorder(grid, row, col, color))
grid = [[1,2,2],[2,3,2]]
row = 0
col = 1
color = 3
print(Solution().colorBorder(grid, row, col, color))