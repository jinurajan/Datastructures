"""
Longest Line of Consecutive One in Matrix

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.

"""
from typing import List


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:

        def dfs(x, y, idx, idy, count):
            nonlocal max_count
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if (x, y) in visited:
                return
            if M[x][y] == 0:
                return
            visited.add((x, y))
            dfs(x+idx, x+idy, idx, idy, count+1)
            max_count = max(count, max_count)
            neighbors = [(1, 1), (-1, 1), (0, 1), (1, 0)]
            for idx, idy in neighbors:
                dfs(x + idx, y + idy, idx, idy, count + 1)

        rows = len(M)
        cols = len(M[0])
        max_count = 0
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    visited = set()
                    dfs(i, j, 0, 0, 0)
        return max_count

input = [[1,1,1,0],
 [1,0,1,1],
 [0,0,0,1]]
print(Solution().longestLine(input))

input = [[1,0,0,0],
 [1,0,1,1],
 [0,0,0,1]]
print(Solution().longestLine(input))