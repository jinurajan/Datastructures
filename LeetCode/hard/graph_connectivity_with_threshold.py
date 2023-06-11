"""
Graph Connectivity With Threshold

We have n cities labeled from 1 to n. Two different cities with labels x and y are directly connected by a bidirectional road if and only if x and y share a common divisor strictly greater than some threshold. More formally, cities with labels x and y have a road between them if there exists an integer z such that all of the following are true:

x % z == 0,
y % z == 0, and
z > threshold.
Given the two integers, n and threshold, and an array of queries, you must determine for each queries[i] = [ai, bi] if cities ai and bi are connected directly or indirectly. (i.e. there is some path between them).

Return an array answer, where answer.length == queries.length and answer[i] is true if for the ith query, there is a path between ai and bi, or answer[i] is false if there is no path.


Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
Output: [false,false,true]
Explanation: The divisors for each number:
1:   1
2:   1, 2
3:   1, 3
4:   1, 2, 4
5:   1, 5
6:   1, 2, 3, 6
Using the underlined divisors above the threshold, only cities 3 and 6 share a common divisor, so they are the
only ones directly connected. The result of each query:
[1,4]   1 is not connected to 4
[2,5]   2 is not connected to 5
[3,6]   3 is connected to 6 through path 3--6

"""

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        self.size = size

    def find(self, u):
        if u != self.root[u]:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.rank[root_p] > self.rank[root_q]:
            self.root[root_q] = root_p
        elif self.rank[root_q] > self.rank[root_p]:
            self.root[root_p] = root_q
        else:
            self.root[root_p] = root_q
            self.rank[root_p] += 1
        
        self.size -= 1
        return True


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n+1)
        for z in range(threshold+1, n+1):
            for x in range(z+z, n+1, z):
                uf.union(z, x)
        result = [False] * len(queries)
        for i, (u,v) in enumerate(queries):
            result[i] = uf.find(u) == uf.find(v)
        return result

