"""
Shortest Path with Alternating Colors
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).



Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""
from typing import List
from collections import defaultdict

inf = float("inf")
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in red_edges:
            graph[u].append((v, 0))
        for u, v in blue_edges:
            graph[u].append((v, 1))
        dist = [[inf] * 2 for _ in range(n)]
        q = [(0, -1)]
        k = 0
        while q:
            new_q = []
            for node, color in q:
                if dist[node][color] > k:
                    dist[node][color] = k
                    for node2, color2 in graph.get(node, []):
                        if color2 != color:
                            new_q.append((node2, color2))
            q = new_q
            k += 1
        return [x if x < inf else -1 for x in map(min, dist)]

n = 3
red_edges = [[0,1],[0,2]]
blue_edges = [[1,0]]
print(Solution().shortestAlternatingPaths(n, red_edges, blue_edges))
