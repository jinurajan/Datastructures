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
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        1. have to go from 1 to 2
        2. cover all zeros in the grid
        3. 4 directional movement

        1. find starting indices ie 1
        2. count the number of zeros to traverse to
        use dfs and increment paths when we reach 2 and we have covered all zeros
        mark visited indices as -2 to avoid calculating duplicate paths
        revert it back once one with one starting point
        """
        total_zeros = 0
        self.total_paths = 0
        start_point = (0, 0)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                   total_zeros += 1
                if grid[i][j] == 1:
                    start_point = (i, j)
        def dfs(x, y, total_zeros):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] < 0:
                return
            if grid[x][y] == 2 and total_zeros == 0:
                self.total_paths += 1
            if grid[x][y] == 0:
                total_zeros -= 1
            neighbors = [[0, 1], [0, -1],[1, 0], [-1, 0]]
            for dx, dy in neighbors:
                tmp = grid[x][y]
                grid[x][y] = -2
                dfs(x+dx, y+dy, total_zeros)
                grid[x][y] = tmp
        dfs(start_point[0], start_point[1], total_zeros)
        return self.total_paths


print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
