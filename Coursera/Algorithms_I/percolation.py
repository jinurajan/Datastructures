"""
Percolation is when you have N*N matrices and we need to check percolated to the bottom without any block

consider 1 - open
0 - close
"""



class Solution(object):
	def flow(self, array):
		n = len(array)
		accessible = []
		for i in range(n):
			a = []
			for j in range(n):
				a.append(0)
			accessible.append(a)
		for j in range(n):
			self._flow(array, accessible, 0, j)
		return accessible


	def _flow(self, array, accessible, i, j):
		n = len(accessible)
		if i <0 or i >=n:
			return
		if j <0 or j >= n:
			return
		if not array[i][j]:
			# value is 0 ie blocked
			return
		if accessible[i][j]:
			# value is already 1
			return
		accessible[i][j] = 1
		neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		for dx, dy in neighbors:
			self._flow(array, accessible, i+dx, j+dy)


	def percolates(self, array):
		accessible = self.flow(array)
		n = len(accessible)
		for j in range(n):
			if accessible[n-1][j]:
				return True
		return False




array = [
[1, 1, 0, 0],
[0, 0, 0, 0],
[1, 1, 1, 0],
[0, 0, 0, 0]
]

print Solution().percolates(array) == False

array = [
[0, 0, 1, 0],
[0, 0, 1, 0],
[1, 1, 1, 0],
[0, 0, 1, 0]
]

print Solution().percolates(array) == True


array = [
[0, 0, 1, 0],
[0, 0, 1, 0],
[1, 1, 1, 0],
[0, 0, 0, 0]
]

print Solution().percolates(array) == False

array = [
[0, 1, 1, 0, 1], 
[0, 0, 1, 1, 1],
[0, 0, 0, 1, 1],
[0, 0, 0, 0, 1],
[0, 1, 1, 1, 1]]
print Solution().percolates(array) == True
