"""
Relax each node n-1 times where n is the total number of edges
"""
from collections import defaultdict

def shortest_path_from_start_end(start, end, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    nodes = graph.keys()
    distance = [float("inf") for i in range(len(nodes)+1)]
    distance[start] = 0
    for i in range(1, len(nodes)):
        for node, edges in graph.items():
            for nei, cost in edges:
                distance[nei] = min(distance[nei], distance[node] + cost)
    print(distance)
    return distance[end]


def shortest_path_from_start_end_optimized(start, end, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    nodes = graph.keys()
    distance = [float("inf") for i in range(len(nodes)+1)]
    distance[start] = 0
    relaxed = True
    for i in range(1, len(nodes)):
        if not relaxed:
            print("breaking at", i)
            break
        for node, edges in graph.items():
            for nei, cost in edges:
                if distance[nei] < distance[node] + cost:
                    relaxed = True
                distance[nei] = min(distance[nei], distance[node] + cost)
    return distance[end]






edges = [[3, 2, 2], [3, 4, 6], [2, 1, 5], [1, 5, 1], [5, 4, 2], [1, 4, 9]]

print(shortest_path_from_start_end(1, 4, edges))
print(shortest_path_from_start_end_optimized(1, 4, edges))
