"""
Number of Provinces


There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # using dfs to find connected components
        rows = len(isConnected)
        visited = set()
        
        def dfs(row):
            for col in range(rows):
                if isConnected[row][col] == 1 and col not in visited:
                    visited.add(col)
                    dfs(col)
        
        count = 0
        for i in range(rows):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count



class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1 for i in range(size)]
        self.count = size

    def find_root(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)

        if root_p != root_q:
            if self.size[root_p] > self.size[root_q]:
                self.root[root_q] = root_p
            elif self.size[root_q] > self.size[root_p]:
                 self.root[root_p] = root_q
            else:
                self.root[root_q] = root_p
                self.size[root_p] += 1
            self.count -= 1
        
    def get_count(self):
        return self.count
    


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected[0]) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.get_count()


      


        