"""
Island Perimeter


You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        def count_neighbors(i, j):
            count = 0
            neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for x, y in neighbours:
                if i + x < 0 or i + x >= rows:
                    count += 1
                    continue
                if j + y < 0 or j + y >= columns:
                    count += 1
                    continue
                if grid[i + x][j + y] == 0:
                    count += 1
            return count
        perimeter = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    perimeter += count_neighbors(i, j)
        return perimeter


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))

grid = [[1]]
print(Solution().islandPerimeter(grid))

grid = [[1,0]]
print(Solution().islandPerimeter(grid))

grid = [[0]]
print(Solution().islandPerimeter(grid))