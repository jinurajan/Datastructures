"""
Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


"""
from typing import List
from heapq import heappop
from heapq import heappush
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(dict)
        nodes = set()
        for (u, v), value in zip(equations, values):
            adj_list[u][v] = value
            adj_list[v][u] = 1.0 / value
            nodes.add(u)
            nodes.add(v)
        
        def find_path(source, nodes):
            # find answer from source to all nodes using dj's algo
            distance = {node: float("inf") for node in nodes}
            distance[source] = 1
            min_heap = [(1, source)]
            visited = set()
            while min_heap:
                w, node = heappop(min_heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, new_w in adj_list[node].items():
                    new_val = new_w * w
                    if new_val < distance[nei]:
                        distance[nei] = new_val
                        heappush(min_heap, (new_val, nei))
            return distance
        
        distances = {}
        for source in nodes:
            distances[source] = find_path(source, nodes)
        
        result = []
        for a, b in queries:
            if a not in distances:
                result.append(-1)
                continue
            r = distances[a].get(b, -1)
            if r == float("inf"):
                r = -1
            result.append(r)

        return result
        

        
