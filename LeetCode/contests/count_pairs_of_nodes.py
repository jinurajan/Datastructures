"""
You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:

a < b
cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be repeated edges.

Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The number of edges incident to at least one of each pair is shown above.

Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]
"""
from typing import List
from collections import Counter

from collections import Counter


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """ TLE """
        node_map, edge_map = Counter(), Counter()
        for x, y in edges:
            node_map[x] += 1
            node_map[y] += 1
            edge_map[min(x, y), max(x, y)] += 1
        pre_compute_dict = {}
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                pre_compute_dict[(i, j)] = node_map[i] + node_map[j] - edge_map.get((i, j), 0)
        result = []
        for query in queries:
            result.append(len([x for x in pre_compute_dict.values() if x > query]))
        return result

from itertools import product

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        node_map, edge_map = {i: 0 for i in range(1, n+1)}, Counter()
        for x, y in edges:
            node_map[x] += 1
            node_map[y] += 1
            edge_map[min(x, y), max(x, y)] += 1
        max_edges = max(node_map.values())
        result = [0 for i in range(2 * max_edges+2)]
        counter = Counter(node_map.values())
        for i, j in product(counter, counter):
            if i < j:
                result[i + j] += counter[i] * counter[j]
            if i == j:
                result[i+j] += counter[i] * (counter[j]-1) // 2

        for (x, y), count in edge_map.items():
            result[node_map[x] + node_map[y]] -= 1
            result[node_map[x] + node_map[y] - count] += 1

        for i in range(len(result)-2, -1, -1):
            result[i] += result[i+1]
        return [result[min(query+1, len(result)-1)] for query in queries]

# n = 4
# edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
# queries = [2,3]
# print(Solution().countPairs(n, edges, queries))
# n = 5
# edges = [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]]
# queries = [1, 2, 3, 4, 5]
# print(Solution().countPairs(n, edges, queries))


n = 5
edges = [[4,5],[1,3],[1,4]]
queries = [0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,2]
print(Solution().countPairs(n, edges, queries))


