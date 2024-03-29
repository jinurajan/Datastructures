"""
Critical Connections in a Network
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.

"""
from typing import List
from collections import defaultdict

class Solution:
    rank = {}
    graph = defaultdict(list)
    conn_dict = {}

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.formGraph(n, connections)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node: int, discovery_rank: int) -> int:
        if self.rank[node]:
            return self.rank[node]
        self.rank[node] = discovery_rank
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def formGraph(self, n: int, connections: List[List[int]]):

        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}

        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None

        for edge in connections:
            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

            self.conn_dict[(min(u, v), max(u, v))] = 1

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(Solution().criticalConnections(n, connections))