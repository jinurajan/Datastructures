"""
Make the tree balanced to keep the quick union faster + with path compression
"""

class QuickUnion:
    def __init__(self, nodes: int):
        """ O(N) """
        self.graph = [i for i in range(nodes)]
        self.node_map = [1 for i in range(nodes)]

    def root(self, i):
        while i != self.graph[i]:
            i = self.graph[self.graph[i]]
        return i

    def union(self, p: int, q: int):
        """ O(logN)"""
        i = root(p)
        j = root(q)
        if i == j:
            return
        if self.node_map[i] < self.node_map[j]:
            id[i] = j
            self.node_map[i] += self.node_map[j]
        else:
            id[j] = i
            self.node_map[j] += self.node_map[i]

    def connected(self, p: int, q: int) -> bool:
        """ O(logN)"""
        return root(p) == root(q)





