"""
 Connecting Cities With Minimum Cost

 There are n cities numbered from 1 to n.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.



Example 1:



Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation:
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation:
There is no way to connect all cities even if all edges are used.


Note:

1 <= n <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= n
0 <= connections[i][2] <= 105
connections[i][0] != connections[i][1]

"""

import heapq


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        parent = [i for i in range(N + 1)]
        rank = [0] * (N + 1)
        connections = [(cost, u, v) for u, v, cost in connections]
        heapq.heapify(connections)
        result = count = 0
        while connections and count < N - 1:
            cost, u, v = heapq.heappop(connections)
            u_parent, v_parent = find(u), find(v)
            if u_parent != v_parent:
                count += 1
                result += cost
                if rank[u_parent] < rank[v_parent]:
                    parent[u_parent] = v_parent
                else:
                    parent[v_parent] = u_parent
                    if rank[u_parent] == rank[v_parent]:
                        rank[u_parent] += 1
        return result if count == N - 1 else -1




