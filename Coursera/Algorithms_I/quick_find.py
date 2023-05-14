"""
Use an array to store the node values and common connected node value


Analysis

Initialize = O(N)
Union - O(N)
connected = O(1) - constant

Union is too expensive as to operate N union operation O(N) will take
total = O(N2) Quadratic



algorithm        initialize       union      find

Quick find        O(N)            O(N)       O(1)


Defects
1. too expensive (N array access on every union operation)
2. Trees are flat. But expensive to keep them flat

"""



class QuickFind():
	def __init__(self, N):
		graph = [0]*N
		for i in range(N):
			graph[i] = i
		self.graph = graph
		self.N = N

	def connected(self, p, q):
		return self.graph[p] == self.graph[q]

	def union(self, p, q):
		pid = self.graph[p]
		qid = self.graph[q]
		for i in range(self.N):
			if self.graph[i] == pid:
				self.graph[i] = qid


q = QuickFind(10)
q.union(1, 2)
q.union(3, 4)
q.union(5, 6)
q.union(0, 5)
q.union(7, 8)
q.union(7, 9)
q.union(1, 9)


print q.connected(2, 9)
print q.graph
print q.connected(2, 3)
print q.connected(0, 6)
print q.connected(4, 0)


