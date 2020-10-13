"""
Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""
from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = set()
        count = 0
        def dfs(u):
            visited.add(u)
            for v in range(n):
                if M[u][v] and v not in visited:
                    dfs(v)
        for u in range(n):
            if u not in visited:
                count += 1
                dfs(u)
        return count



class Solution1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        count = 0
        visited = set()
        for u in range(n):
            if u not in visited:
                count += 1
                visited.add(u)
                q = [u]
                while q:
                    v = q.pop(0)
                    visited.add(v)
                    for j in range(n):
                        if M[v][j] and j not in visited:
                            q.append(j)
                            visited.add(j)
        return count

    


M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
print(Solution().findCircleNum(M))
print(Solution1().findCircleNum(M))

M = [[1,0,0],[0,1,0],[0,0,1]]

print(Solution().findCircleNum(M))
print(Solution1().findCircleNum(M))


M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNum(M))
print(Solution1().findCircleNum(M))
