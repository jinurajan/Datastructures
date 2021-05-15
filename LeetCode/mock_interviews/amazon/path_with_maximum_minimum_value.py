"""
Path With Maximum Minimum Value


Given a matrix of integers grid with m rows and n columns, find the maximum score of a path starting at [0,0] and ending at [m-1,n-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).



Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3


Note:

1 <= m, n <= 100
0 <= grid[i][j] <= 109
"""

import heapq


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_score = float("inf")
        end = [rows - 1, cols - 1]
        visited = set()
        max_heap = []
        heapq.heappush(max_heap, (-grid[0][0], (0, 0)))
        while max_heap:
            val, (x, y) = heapq.heappop(max_heap)
            val *= -1
            max_score = min(max_score, val)
            if [x, y] == end:
                return max_score
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in neighbors:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= rows - 1 and 0 <= new_y <= cols - 1 and (new_x, new_y) not in visited:
                    heapq.heappush(max_heap, (-1 * grid[new_x][new_y], (new_x, new_y)))
        return max_score








