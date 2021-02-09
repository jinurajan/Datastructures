"""
Number of Distinct Islands
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011

11011
10000
00001
11011

"""
from typing import List

class Solution2:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        rows = len(grid)

        def is_island_unique():
            for island in islands:
                if len(island) != len(curr_island):
                    continue
                else:
                    for cell_1, cell_2 in zip(island, curr_island):
                        if cell_1 != cell_2:
                            break
                    else:
                        return False
            return True

        def dfs(node, i, j):
            if i < 0 or i > rows-1 or j < 0 or j > columns-1:
                return
            if (i, j) in visited or not node[i][j]:
                return
            visited.add((i, j))
            curr_island.append((i-row_origin, j-col_origin))
            neighbor_idx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in neighbor_idx:
                dfs(node, i+x, j+y)

        visited = set()
        islands = []
        for i in range(rows):
            for j in range(columns):
                curr_island = []
                row_origin = i
                col_origin = j
                dfs(grid, i, j)
                if not curr_island or not is_island_unique():
                    continue
                islands.append(curr_island)
        return len(islands)



class Solution1:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        rows = len(grid)
        def dfs(node, i, j):
            if i < 0 or i > rows-1 or j < 0 or j > columns-1:
                return
            if (i, j) in visited or not node[i][j]:
                return
            visited.add((i, j))
            curr_island.append((i-row_origin, j-col_origin))
            neighbor_idx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in neighbor_idx:
                dfs(node, i+x, j+y)

        visited = set()
        islands = set()
        for i in range(rows):
            for j in range(columns):
                curr_island = []
                row_origin = i
                col_origin = j
                dfs(grid, i, j)
                if curr_island:
                    islands.add(frozenset(curr_island))
        return len(islands)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        rows = len(grid)
        def dfs(node, i, j, direction):
            if i < 0 or i > rows-1 or j < 0 or j > columns-1:
                return
            if (i, j) in visited or not node[i][j]:
                return
            visited.add((i, j))
            path.append(direction)
            neighbor_idx = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
            for x, y, direction in neighbor_idx:
                dfs(node, i+x, j+y, direction)
            path.append("0")

        visited = set()
        islands = set()
        for i in range(rows):
            for j in range(columns):
                path = []
                dfs(grid, i, j, "0")
                if path:
                    islands.add(tuple(path))
        return len(islands)





grid = [[1,1,0,1,1],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1]]
print(Solution().numDistinctIslands(grid) == 3)

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

print(Solution().numDistinctIslands(grid) == 1)

grid = [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]
print(Solution().numDistinctIslands(grid) == 2)




