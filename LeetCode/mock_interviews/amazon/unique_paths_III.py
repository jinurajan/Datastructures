"""
Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Note:

1 <= grid.length * grid[0].length <= 20
"""


class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        self.res = 0
        empty, m, n = 1, len(A), len(A[0])

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(empty, x, y):
            if not (0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] >= 0):
                return

            if A[x][y] == 2:
                self.res += empty == 0
                return

            A[x][y] = -2
            dfs(empty - 1, x + 1, y)
            dfs(empty - 1, x - 1, y)
            dfs(empty - 1, x, y + 1)
            dfs(empty - 1, x, y - 1)
            A[x][y] = 0

        dfs(empty, x, y)
        return self.res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        end = None
        start = None
        non_obstacles = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    end = [i, j]
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] >= 0:
                    non_obstacles += 1
        if start is None or end is None:
            return 0
        neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        count = 0

        def is_valid(x, y):
            return 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and grid[x][y] >= 0

        def dfs(x, y, non_obstacles):
            nonlocal count
            if [x, y] == end and non_obstacles == 1:
                count += 1
                return
            tmp = grid[x][y]
            grid[x][y] = -4
            for dx, dy in neighbors:
                if is_valid(x + dx, y + dy):
                    dfs(x + dx, y + dy, non_obstacles - 1)
            grid[x][y] = tmp

        dfs(start[0], start[1], non_obstacles)
        return count