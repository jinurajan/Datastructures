"""
Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # BFS 
        if not heights or not heights[0]:
            return
        rows = len(heights)
        cols = len(heights[0])

        pacific_q = deque()
        atlantic_q = deque()
        for i in range(rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, cols-1))
        for j in range(cols):
            pacific_q.append((0, j))
            atlantic_q.append((rows-1, j))
        
        def bfs(queue):
            visited = set()

            while queue:
                i, j = queue.popleft()
                visited.add((i, j))
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in neighbors:
                    x, y = i+dx, j+dy
                    if not(0 <=x <= rows-1)or not(0 <= y <= cols-1):
                        continue
                    if (x,y) in visited or heights[x][y] < heights[i][j]:
                        continue
                    queue.append((x,y))
            return visited
        
        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)
        return list(pacific_reachable.intersection(atlantic_reachable))
                    

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # DFS 
        if not heights or not heights[0]:
            return
        rows = len(heights)
        cols = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(x, y, reachable):
            reachable.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x,new_y = x+dx, y+dy
                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                    continue
                if((new_x, new_y)) in reachable:
                    continue
                if heights[new_x][new_y] < heights[x][y]:
                    # cannot flow from x, y if heights are atleast equal or greater than parent
                    continue

                dfs(new_x, new_y, reachable)
        
        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols-1, atlantic_reachable)
        
        for i in range(cols):
            dfs(0, i, pacific_reachable)
            dfs(rows-1, i, atlantic_reachable)
        
        return list(pacific_reachable.intersection(atlantic_reachable))
        




