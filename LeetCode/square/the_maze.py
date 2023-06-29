"""
The Maze


There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Thoughts

1. use bfs from starting indices. every time roll until it cannot roll any more from a location

"""
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])

        queue = [start]
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_valid(x, y):
            return 0<=x<rows and 0<=y<cols

        while queue:
            x, y = queue.pop(0)
            if [x, y] == destination:
                return True
            for dx, dy in directions:
                x1, y1 = x+dx, y+dy
                while is_valid(x1, y1) and maze[x1][y1] == 0:
                    x1 += dx
                    y1 += dy
                rolled_to_x = x1-dx
                rolled_to_y = y1-dy
                if (rolled_to_x, rolled_to_y) not in visited:
                    visited.add((rolled_to_x, rolled_to_y))
                    queue.append([rolled_to_x, rolled_to_y])

        return False
            



    