"""
Relax the nodes starting from the start node

Use priority queue to get the node with lowest cost or path distance
"""
from collections import defaultdict
import heapq

def shortest_path(start, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    nodes = graph.keys()
    distance = [float("inf") for i in range(len(nodes)+1)]
    print(distance)
    distance[start] = 0
    visited = set()
    min_heap = [(0, start)]
    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        for edge in graph[node]:
            nei, d = edge[0],edge[1]
            new_dist = distance[node] + d
            if new_dist < distance[nei]:
                distance[nei] = new_dist
                heapq.heappush(min_heap, (new_dist, nei))
    return distance




def shortest_path_from_start_end(start, end, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    nodes = graph.keys()
    distance = [float("inf") for i in range(len(nodes)+1)]
    print(distance)
    distance[start] = 0
    visited = set()
    min_heap = [(0, start)]
    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        for edge in graph[node]:
            nei, d = edge[0],edge[1]
            new_dist = distance[node] + d
            if new_dist < distance[nei]:
                distance[nei] = new_dist
                heapq.heappush(min_heap, (new_dist, nei))
    return distance[nei]

edges = [[3, 2, 2], [3, 4, 6], [2, 1, 5], [1, 5, 1], [5, 4, 2], [1, 4, 9]]

print(shortest_path(1, edges))
print(shortest_path_from_start_end(1, 4, edges))

