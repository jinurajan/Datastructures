"""
Lazy approach 
Each node will contain the parents value

Find the root by recursively checking the value until values are same

To find if two nodes connected: check if roots are same

Union:  To connect P and Q

set the id of root(P) to id of Q's root (Only One value changes)


algorithm        initialize              union                 find

Quick find        O(N)                    O(N)                 O(1)
Quick Union       O(N)                    O(N)                 O(N) ---- worst case
Weighted Quick Union  O(N) + O(N)        O(log N)              O(logN) --- worst case depends on depth(p) and depth(q). ie max(depth(q), depth(q))

Depth of any node x is maximum LogN

"""
class QuickUnionWeighted():
	def __init__(self, N):
		graph = [0]*N
		for i in range(N):
			graph[i] = i
		self.graph = graph
		self.size = [0]*N
		self.N = N

	def root(self, i):
		while i != self.graph[i]:
			i = self.graph[i]
		return i


	def connected(self, p, q):
		return self.root(p) == self.root(q)
		

	def union(self, p, q):
		rootp = self.root(p)
		rootq = self.root(q)
		if rootp == rootq:
			return
		if self.size[rootp] < self.size[rootq]:
			self.graph[rootp] = self.graph[rootq]
			self.size[rootq] += self.size[rootp]
		else:
			self.graph[rootq] = self.graph[rootp]
			self.size[rootp] += self.size[rootq]




q = QuickUnionWeighted(10)
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


		

