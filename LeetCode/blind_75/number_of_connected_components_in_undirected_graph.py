"""
Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

"""
from typing import List
from collections import defaultdict



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            unionFind = WeightedPathCompressionQuickUnionUF(n)
            components = n
            for u, v in edges:
                if unionFind.union(u, v):
                    components -= 1
            return components

class WeightedPathCompressionQuickUnionUF:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.N = N
    
    def find(self, node):
        while self.root[node] != node:
            self.root[node] = self.root[self.root[node]]
            node = self.root[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return False
        if self.rank[p] < self.rank[q]:
            self.root[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        else:
            self.root[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        return True
       