"""
Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.



Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


Constraints:

|x| + |y| <= 300
"""


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        neighbors = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        start_q = [(0, 0, 0)]
        start_visited = {(0, 0): 0}
        end_q = [(x, y, 0)]
        end_visited = {(x, y): 0}

        while True:
            start_x, start_y, start_dist = start_q.pop(0)
            if (start_x, start_y) in end_visited:
                return start_dist + end_visited[(start_x, start_y)]

            end_x, end_y, end_dist = end_q.pop(0)
            if (end_x, end_y) in start_visited:
                return end_dist + start_visited[(end_x, end_y)]

            for dx, dy in neighbors:
                new_start_x, new_start_y = start_x + dx, start_y + dy
                if (new_start_x, new_start_y) not in start_visited:
                    start_q.append((new_start_x, new_start_y, start_dist + 1))
                    start_visited[(new_start_x, new_start_y)] = start_dist + 1
                new_end_x, new_end_y = end_x + dx, end_y + dy
                if (new_end_x, new_end_y) not in end_visited:
                    end_q.append((new_end_x, new_end_y, end_dist + 1))
                    end_visited[(new_end_x, new_end_y)] = end_dist + 1