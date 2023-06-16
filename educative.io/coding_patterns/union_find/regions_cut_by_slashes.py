"""
An n×n grid is composed of n 1*1 squares, where each 1×1 square consists of a “/”, “\”, or a blank space. These characters divide the square into adjacent regions.

Given the grid represented as a string array, return the number of adjacent regions.
"""

class UnionFind:
    # Constructor
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [1] * n
        for i in range(n):
            self.parent[i] = i
        
    # Function to find which subset a particular element belongs to.
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    # Function to join two subsets into a single subset.
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] = self.rank[p1] + self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] = self.rank[p2] + self.rank[p1]


def regions_by_slashes(grid):
    N = len(grid)
    union_find = UnionFind(4 * N * N)

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            root = 4 * (r*N +c)

            if val in '/ ':
                union_find.union(root+0, root+1)
                union_find.union(root+2, root+3)
            
            if val in '\ ':
                union_find.union(root+0, root+2)
                union_find.union(root+1, root+3)
            
            if r + 1 < N:
                union_find.union(root+3, (root+4*N)+0)
            
            if r-1 >= 0:
                union_find.union(root+0, (root-4*N)+3)
            
            if c+1 < N:
                union_find.union(root+2, (root+4)+1)
            
            if c-1 >= 0:
                union_find.union(root+1, (root-4)+2)
    return sum(union_find.find(x) == x for x in range(4 * N * N))
