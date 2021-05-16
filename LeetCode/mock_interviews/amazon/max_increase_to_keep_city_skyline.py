"""
Max Increase to Keep City Skyline

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation:
The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        total_increase = 0
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                total_increase += min(row_maxes[row_idx], col_maxes[col_idx]) - grid[row_idx][col_idx]

        return total_increase


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_col = [0 for i in range(cols)]
        max_row = [0 for i in range(rows)]

        for i in range(rows):
            max_row[i] = max(grid[i])
        i = 0
        while i < rows:
            max_val = 0
            for j in range(cols):
                max_val = max(grid[j][i], max_val)
            max_col[i] = max_val
            i += 1
        max_sum = 0
        for i in range(rows):
            for j in range(cols):
                diff = min(max_row[i], max_col[j])
                max_sum += diff - grid[i][j]
                grid[i][j] = diff

        return max_sum
