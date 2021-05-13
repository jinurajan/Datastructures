"""
The Maze II
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: -1
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: -1
"""

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        if m == 0:
            return -1
        n = len(maze[0])
        if n == 0:
            return -1

        # 4 one-step move directions
        drs = [(-1,0),(1,0),(0,1),(0,-1)]

        def one_direction(last_x, last_y, dr):
            # Calculate moving cost for the ball starting at [last_x, last_y]
            # and move along one direction, as well as the final position [x, y]
            x, y = last_x, last_y
            moving_cost = 0
            while True:
                if 0 <= x+dr[0] < m and 0 <= y+dr[1] < n and maze[x+dr[0]][y+dr[1]] == 0:
                    moving_cost += 1
                    x += dr[0]
                    y += dr[1]
                else:
                    break

            return moving_cost, x, y

        # Setup for Dijkstra
        seen = [[float('inf') for _ in range(n)] for _ in range(m)]    # minimum distance so far
        sp = [start]    # record the shortest path
        h = [(0, start[0], start[1], sp)]   # min-heap

        while h:
            # Fetch the current minimum cost node,
            # as the next starting point
            cost, x, y, cur_sp = heapq.heappop(h)
            if x == destination[0] and y == destination[1]:
                # Found the minimum distance path to the destination
                return cost

            for d in drs:
                dist, dr_x, dr_y = one_direction(x, y, d)
                dr_cost = cost+dist
                if seen[dr_x][dr_y] > dr_cost:
                    seen[dr_x][dr_y] = dr_cost
                    heapq.heappush(h, (dr_cost, dr_x, dr_y, cur_sp+[[dr_x, dr_y]]))

		# Destination unreachable
        return -1