"""
Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        def dfs(i, j, paths):
            paths.add((i, j))
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for idx, idy in neighbors:
                x, y = i+idx, j+idy
                if x < 0 or x >= rows or y < 0 or y >= cols:
                    continue
                if (x, y) in paths or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(x, y, paths)

        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols-1, atlantic_reachable)
        for i in range(cols):
            dfs(0, i, pacific_reachable)
            dfs(rows-1, i, atlantic_reachable)
        return list(pacific_reachable.intersection(atlantic_reachable))


from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols-1))
        for i in range(cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((rows - 1, i))

        def bfs(queue):
            visited = set()
            while queue:
                i, j = queue.popleft()
                visited.add((i, j))
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for idx, idy in neighbors:
                    x, y = i + idx, j + idy
                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        continue
                    if (x, y) in visited or matrix[x][y] < matrix[i][j]:
                        continue
                    queue.append((x, y))
            return visited
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        return list(pacific_reachable.intersection(atlantic_reachable))








matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(Solution().pacificAtlantic(matrix))