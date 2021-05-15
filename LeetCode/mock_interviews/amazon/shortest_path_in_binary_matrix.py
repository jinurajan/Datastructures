"""
Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

"""

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        Q = deque([(0, 0)])
        rows = len(grid)
        columns = len(grid[0])
        grid[0][0] = 1
        def is_valid(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j]:
                return False
            return True
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while Q:
            i, j = Q.popleft()
            path = grid[i][j]
            if i == rows-1 and j == columns -1:
                return path
            for x, y in neighbours:
                if is_valid(i+x, j+y):
                    grid[i+x][j+y] = path + 1
                    Q.append((i+x, j+y))
        if grid[-1][-1] == 0:
            return -1
        return grid[-1][-1]
