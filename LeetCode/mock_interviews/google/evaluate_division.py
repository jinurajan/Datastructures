"""
Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        nodes = set()
        for i, (u, v) in enumerate(equations):
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
            nodes.add(u)
            nodes.add(v)

        def find_paths(source, nodes):
            distance = {node: float("inf") for node in nodes}
            distance[source] = 1
            visited = set()
            min_heap = [(1, source)]
            while min_heap:
                d, node = heapq.heappop(min_heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, w in graph[node].items():
                    new_val = d * w
                    if new_val < distance[nei]:
                        distance[nei] = new_val
                        heapq.heappush(min_heap, (new_val, nei))
            return distance

        distances = {}
        for source in nodes:
            distances[source] = find_paths(source, nodes)
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

from collections import defaultdict
from itertools import chain

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(start_node, comp, w):
            self.weights[start_node] = [comp, w]
            for j, weight in self.edges[start_node].items():
                if self.weights[j][0] == -1:
                    dfs(j, comp, w / weight)

        nodes = set(chain(*equations))
        result = []
        v = 0
        self.edges = defaultdict(dict)
        for idx, [i, j] in enumerate(equations):
            self.edges[i][j] = values[idx]
            self.edges[j][i] = 1/values[idx]
        self.weights = defaultdict(list)
        for node in nodes:
            self.weights[node] = [-1, -1]
        # v is to denote maximum number of components.start with 0th component
        for node in nodes:
            if self.weights[node][0] == -1:
                dfs(node, v, 1)
                v += 1
        for a, b in queries:
            if a not in nodes or b not in nodes or self.weights[a][0] != self.weights[b][0]:
                result.append(-1)
            elif a == b:
                result.append(1)
            else:
                result.append(self.weights[a][1] / self.weights[b][1])
        return result
