"""
K Highest Ranked Items Within a Price Range


You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.

You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.




"""
from typing import List
from heapq import *
from collections import defaultdict


from heapq import *
from collections import defaultdict

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:

        R, C = map(len, (grid, grid[0]))
        ans, (x, y), (low, high) = [], start, pricing
        heap = [(0, grid[x][y], x, y)]
        seen = {(x, y)}
        while heap and len(ans) < k:
            distance, price, r, c = heappop(heap)
            if low <= price <= high:
                ans.append([r, c])
            for i, j in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                if R > i >= 0 <= j < C and grid[i][j] > 0 and (i, j) not in seen: 
                    seen.add((i, j))
                    heappush(heap, (distance + 1, grid[i][j], i, j))
        return ans



class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows = len(grid)
        if not rows or grid[start[0]][start[1]] == 0:
            return []
        
        cols = len(grid[0])

        def is_valid(i, j):
            return 0<=i<rows and 0<=j<cols and grid[i][j] != 0
        
        distance = defaultdict(lambda:float("inf"))
        distance[(start[0], start[1])] = 0
        visited = set()
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        min_heap = [(0, (start[0], start[1]))]

        while min_heap:
            dist, (x, y) = heappop(min_heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in neighbours:
                new_x, new_y = x+dx, y+dy
                if is_valid(new_x, new_y):
                    new_dist = distance[(x, y)] + 1
                    if new_dist < distance[(new_x,new_y)]:
                        distance[(new_x,new_y)] = new_dist
                        heappush(min_heap, (new_dist, (new_x, new_y)))
        
        result = []
        for node, dist in distance.items():
            if pricing[0] <= grid[node[0]][node[1]] <= pricing[1]:
                result.append((dist, grid[node[0]][node[1]], node[0], node[1]))
        result.sort()
        return [(val[2], val[3]) for val in result[:k]]


grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2,5]
start = [0,0]
k = 3
print(Solution().highestRankedKItems(grid=grid, pricing=pricing, start=start, k=k))
grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]]
pricing = [2,3]
start = [2,3]
k = 2
print(Solution().highestRankedKItems(grid=grid, pricing=pricing, start=start, k=k))