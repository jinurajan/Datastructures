



class QuickFind:
    def __init__(self, nodes: int):
        """ O(N) """
        self.graph = [i for i in range(nodes)]

    def union(self, p: int, q: int):
        """ O(N) """
        p_id = self.graph[p]
        q_id = self.graph[q]
        for i in range(len(self.graph)):
            if self.graph[i] == p_id:
                id[i] = q_id

    def connected(self, p: int, q: int) -> bool:
        """ O(1) """
        return self.graph[p] == self.graph[q]





