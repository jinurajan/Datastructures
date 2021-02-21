"""
Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
from typing import List
from collections import defaultdict

class Solution2:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        def find_buildings_obstacles_lands(rows, cols):
            nonlocal buildings, obstacles, lands
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        buildings.add((i, j))
                    elif grid[i][j] == 2:
                        obstacles.add((i, j))
                    else:
                        lands.add((i, j))

        def find_distances(x, y, i, j, rows, cols, dist):
            nonlocal building_map
            if (i, j) in buildings:
                building_map[(i, j)] = min(building_map[(i, j)], dist)
                return
            elif (i, j) in obstacles:
                return
            else:
                if (i, j) not in visited_nodes:
                    visited_nodes.add((i, j))
                else:
                    return
                neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]
                for idx, idy in neighbors:
                    if i+idx < 0 or i+idx  >= rows or j+idy < 0 or j+idy >= cols:
                        continue
                    find_distances(x, y, i+idx, j+idy, rows, cols, dist+1)
        rows = len(grid)
        cols = len(grid[0])
        buildings = set()
        obstacles = set()
        lands = set()
        find_buildings_obstacles_lands(rows, cols)
        min_dist = float("inf")
        for x, y in lands:
            building_map = defaultdict(lambda:float("inf"))
            visited_nodes = set()
            find_distances(x, y, x, y, rows, cols, 0)
            if len(building_map) != len(buildings):
                return -1
            total_dist = sum(building_map.values())
            min_dist = min(total_dist, min_dist)
        if min_dist == float("inf") or min_dist == 0:
            return -1
        return min_dist


from collections import deque
class Solution1:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        rows = len(grid)
        cols = len(grid[0])

        def bfs(i, j):
            neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            queue = deque([(i, j)])
            visited = set()
            distance = 0
            while queue:
                distance += 1
                size = len(queue)
                while size:
                    x, y = queue.popleft()
                    for idx, idy in neighbors:
                        if x+idx >=0 and x+idx < rows and y+idy >=0 and y+idy < cols and not grid[x+idx][y+idy] and (x+idx, y+idy) not in visited:
                            visited.add((x+idx, y+idy))
                            dist_matrix[x+idx][y+idy] += distance
                            num_matrix[x+idx][y+idy] += 1
                            queue.append((x+idx, y+idy))
                    size -= 1

        dist_matrix = [[0 for i in range(cols)] for j in range(rows)]
        num_matrix = [[0 for i in range(cols)] for j in range(rows)]
        buildings = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i, j)
        min_dist = float("inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and dist_matrix[i][j] != 0 and num_matrix[i][j] == buildings:
                    min_dist = min(min_dist, dist_matrix[i][j])
        if min_dist < float("inf"):
            return min_dist
        return  -1

from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        buildings = sum(val for row in grid for val in row if val == 1)
        dist_matrix = [[0 for i in range(cols)] for j in range(rows)]
        num_matrix = [[0 for i in range(cols)] for j in range(rows)]
        def bfs(i, j):
            neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            queue = deque([(i, j, 0)])
            visited = set((i, j))
            count = 1
            while queue:
                x, y, distance = queue.popleft()
                for idx, idy in neighbors:
                    if x+idx >=0 and x+idx < rows and y+idy >=0 and y+idy < cols and (x+idx, y+idy) not in visited:
                        if not grid[x + idx][y + idy]:
                            visited.add((x+idx, y+idy))
                            dist_matrix[x+idx][y+idy] += distance + 1
                            num_matrix[x+idx][y+idy] += 1
                            queue.append((x+idx, y+idy, distance+1))
                        elif grid[x+idx][y+idy] == 1:
                            count += 1
            print(count, buildings)
            return count == buildings

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1
        return min(
            [dist_matrix[i][j] for i in range(rows) for j in range(cols) if not grid[i][j] and num_matrix[i][j] == buildings] or [-1])






grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(Solution().shortestDistance(grid))
grid = [[1]]
print(Solution().shortestDistance(grid))
grid = [[1, 2, 0]]
print(Solution().shortestDistance(grid))
grid = [[0,2,1],[1,0,2],[0,1,0]]
print(Solution().shortestDistance(grid))

# grid = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]
# print(Solution().shortestDistance(grid))


