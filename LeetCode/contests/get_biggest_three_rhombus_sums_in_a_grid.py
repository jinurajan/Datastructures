"""
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.



Example 1:
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
"""
from typing import List
from heapq import heappushpop, heappop,heappush

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        sums = []
        rows = len(grid)
        cols = len(grid[0])
        # prefix diagonal sum
        grid.append([(0, 0)] * (cols + 1))
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = (grid[i][j] + grid[i - 1][j - 1][0], grid[i][j] + grid[i - 1][j + 1][1])
            grid[i].append((0, 0))
        h = []
        # k - romb size
        for k in range((min(rows, cols) + 1) // 2):
            # (i, j) - romb center position
            for i in range(k, rows - k):
                for j in range(k, cols - k):
                    if k == 0:
                        s = grid[i][j][0] - grid[i - 1][j - 1][0]
                    else:
                        left_top = grid[i][j - k][1] - grid[i - k - 1][j + 1][1]
                        right_top = grid[i][j + k][0] - grid[i - k][j][0]
                        left_bottom = grid[i + k][j][0] - grid[i][j - k][0]
                        right_bottom = grid[i + k - 1][j + 1][1] - grid[i][j + k][1]
                        s = left_top + right_top + left_bottom + right_bottom

                    if s not in h:
                        if len(h) < 3:
                            heappush(h, s)
                        else:
                            heappushpop(h, s)
        h.sort(reverse=True)
        return h


grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
print(Solution().getBiggestThree(grid))