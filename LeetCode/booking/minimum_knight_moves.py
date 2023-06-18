"""
Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.


1. BFS  and keep track to distance and meet in the middle (try from both ends)
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        neighbours = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        start_q = [(0, 0, 0)]
        end_q = [(x, y, 0)]
        
        start_visited = {(0, 0): 0}
        end_visited = {(x, y): 0}
        while True:
            start_i, start_j, start_dist = start_q.pop(0)
            if (start_i, start_j) in end_visited:
                return start_dist + end_visited[(start_i, start_j)]
            
            end_i, end_j, end_dist = end_q.pop(0)
            if (end_i, end_j) in start_visited:
                return end_dist + start_visited[(end_i, end_j)]
            for dx, dy in neighbours:
                start_x, start_y = start_i+dx, start_j+dy
                if (start_x, start_y) not in start_visited:
                    start_q.append((start_x, start_y, start_dist+1))
                start_visited[(start_x, start_y)] = start_dist + 1
                
                end_x, end_y = end_i+dx, end_j+dy
                if (end_x, end_y) not in end_visited:
                    end_q.append((end_x, end_y, end_dist+1))
                end_visited[(end_x, end_y)] = end_dist + 1