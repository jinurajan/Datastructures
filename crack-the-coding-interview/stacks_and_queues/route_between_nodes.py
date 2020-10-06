"""
Route between two nodes. Find if there exists a path between two nodes

"""



from collections import deque


def bfs(graph, start, end):
	if start == end:
		return True
	visited = set()
	visited.add(start)
	q = deque()
	q.append(start)
	while len(q) > 0:
		u = q.pop()
		if u:
			for v in graph.get(u, []):
				if v not in visited:
					if v == end:
						return True
					visited.add(v)
					q.append(v)
		visited.add(u)
	return False




graph = {
0: [1, 4, 5],
1: [4, 3],
2: [1],
3: [2, 4]
}

print(bfs(graph, 1, 2))
print(bfs(graph, 5, 0))


