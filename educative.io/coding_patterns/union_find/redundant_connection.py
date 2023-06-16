"""
We are given an undirected graph consisting of n nodes. The graph is represented as list called edges, of length n, where edges[i] = [a, b] indicates that there is an edge between nodes a and b in the graph.

Return an edge that can be removed to make the graph a tree of n nodes. If there are multiple candidates for removal, return the edge that occurs last in edges.
"""

class UnionFind:

    # Constructor
    def __init__(self, n):
        self.parent = []
        for i in range(n + 1):
            self.parent.append(i)
        self.rank =[1] * (n+1)

    # Function to find which subset a particular element belongs to
    def find_parent(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]
   
    # Function to join two subsets into a single subset
    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            return False
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True


def redundant_connection(edges):
    uf = UnionFind(len(edges))
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]


def main():
	edges = [
		[[1, 2], [1, 3], [2, 3]], 
		[[1, 2], [2, 3], [1, 3]], 
		[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], 
		[[1, 2], [1, 3], [1, 4], [3, 4], [2, 4]], 
		[[1, 2], [1, 3], [1, 4], [1,5], [2, 3], [2, 4], [2, 5]]
	]

	for i in range(len(edges)):
		print(i+1, ".\tEdges: ", edges[i], sep = "")
		print("\tThe redundant connection in the graph is: ", redundant_connection(edges[i]), sep = "")
		print("-" * 100)

if __name__ == '__main__':
	main()