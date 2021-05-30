"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.
"""
from collections import defaultdict

def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order
    in_degree = {i: 0 for i in range(vertices)}
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    sources = [k for k, v in in_degree.items() if v == 0]
    while sources:
        v = sources.pop(0)
        sorted_order.append(v)
        for nei in graph[v]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                sources.append(nei)
    if len(sorted_order) != vertices:
        # graph has a cycle
        return []
    return sorted_order



print("Topological sort: " + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
print("Topological sort: " + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
print("Topological sort: " + str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


