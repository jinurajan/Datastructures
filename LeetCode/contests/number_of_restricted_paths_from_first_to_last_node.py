"""

"""
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if not edges or n == 1:
            return 0
        adj_map = defaultdict(dict)
        for x, y, weight in edges:
            adj_map[x][y] = weight
            adj_map[y][x] = weight
        dfs_mem = {}
        def dijsktra():
            minheap = [(0, n)]
            dist = [float("inf")] * (n + 1)
            dist[n] = 0
            while minheap:
                distance, node = heappop(minheap)
                if distance != dist[node]:
                    continue
                for v, weight in adj_map[node].items():
                    if dist[v] > dist[node] + weight:
                        dist[v] = dist[node] + weight
                        heappush(minheap, (dist[v], v))
            return dist
        def dfs(node):
            if node == n:
                return 1
            if node in dfs_mem:
                return dfs_mem[node]
            ans = 0
            for nei, weight in adj_map[node].items():
                if dist[node] > dist[nei]:
                    ans =  (ans + dfs(nei)) % 1000000007
            dfs_mem[node] = ans
            return ans
        dist = dijsktra()
        return dfs(1)





n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(Solution().countRestrictedPaths(n, edges))
# n = 7
# edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
# print(Solution().countRestrictedPaths(n, edges))