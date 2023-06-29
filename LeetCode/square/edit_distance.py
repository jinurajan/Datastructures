"""
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
"""
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp using lru_cache
        @lru_cache(maxsize=None)
        def min_distance(idx1, idx2):
            if idx1 ==  0:
                return idx2
            if idx2 == 0:
                return idx1
            if word1[idx1-1] == word2[idx2-1]:
                return min_distance(idx1-1, idx2-1)
            else:
                return min(
                    min_distance(idx1-1, idx2-1),
                    min_distance(idx1, idx2-1),
                    min_distance(idx1-1, idx2),
                ) + 1

        return min_distance(len(word1), len(word2))
    

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp using array
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]* (n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            dp[i][0] = i

        for j in range(1, n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1],
                        dp[i-1][j],
                        dp[i][j-1])  + 1
        return dp[n1][n2] 




from collections import deque
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # using bfs 
        if word1 == word2:
            return 0
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        
        w1 = list(word1)
        w2 = list(word2)

        num = 0
        queue = deque()
        queue.append((0, 0))
        visited = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                    i += 1
                    j += 1
                if i == len(w1) and j == len(w2):
                    return num
                queue.append((i, j+1))
                queue.append((i+1, j+1))
                queue.append((i+1, j))
            num += 1
        
        return num