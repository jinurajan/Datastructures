"""
Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        if rows == 0:
            return
        cols = len(rooms[0])
        GATE = 0
        EMPTY = pow(2, 31) - 1
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == GATE:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for idx, idy in DIRECTIONS:
                if x + idx < 0 or x + idx >= rows or y + idy < 0 or y + idy >= cols or rooms[x + idx][y + idy] != EMPTY:
                    continue
                rooms[x + idx][y + idy] = rooms[x][y] + 1
                q.append((x + idx, y + idy))

