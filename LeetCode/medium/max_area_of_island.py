"""
Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]:

                    # start tree traversal with (r, c) as root
                    nodes, carea = {(r, c)}, 0
                    while nodes:
                        cr, cc = nodes.pop()
                        grid[cr][cc] = 0
                        carea += 1
                        if cc - 1 >= 0 and grid[cr][cc - 1]:
                            nodes.add((cr, cc - 1))
                        if cr - 1 >= 0 and grid[cr - 1][cc]:
                            nodes.add((cr - 1, cc))
                        if cc + 1 <= n - 1 and grid[cr][cc + 1]:
                            nodes.add((cr, cc + 1))
                        if cr + 1 <= m - 1 and grid[cr + 1][cc]:
                            nodes.add((cr + 1, cc))
                    ans = max(ans, carea)
        return ans
