"""
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.



Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses

Thoughts

1. topological sorting. if there is a cycle topological sorting is not possible

algorithm
1. 

"""

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        q = deque()
        # fetch those with no indegree to be processed first
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        nodesVisited = 0
        while q:
            # bfs
            node = q.popleft()
            nodesVisited += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1
                # when indegree is zero ie no dependencies add it to queue
                if indegree[neigh] == 0:
                    q.append(neigh)
        return nodesVisited == numCourses


class Solution:

    def dfs(self, node, adj, visited, instack):
        if instack[node]:
            # there is a cycle 
            return True
        if visited[node]:
            return False
        
        visited[node] = True
        instack[node] = True
        for neigh in adj[node]:
            if self.dfs(neigh, adj, visited, instack):
                return True
        instack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use two one for inprogress node one for completed nodes
        adj = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
        
        visited = [False] * numCourses
        instack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visited, instack):
                return False
        return True

