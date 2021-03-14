



class QuickUnion:
    def __init__(self, nodes: int):
        """ O(N) """
        self.graph = [i for i in range(nodes)]

    def root(self, i):
        while i != self.graph[i]:
            i = self.graph[i]
        return i

    def union(self, p: int, q: int):
        """ O(N)"""
        i = root(p)
        j = root(q)
        id[i] = j

    def connected(self, p: int, q: int) -> bool:
        """ O(N)"""
        return root(p) == root(q)





