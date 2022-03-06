

from functools import lru_cache
from typing import List
from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = [set() for _ in range(n)]
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            result[v].add(u)
            graph[u].append(v)
            in_degree[v] += 1
        
        #topoological sort: start with those with indegree 0 #bfs
        dq = deque([u for u, degree in enumerate(in_degree) if degree==0])
        while dq:
            node = dq.popleft()
            for neighbor in graph[node]:
                # if 3 -> 5 then add 3's ancestors to the list
                result[neighbor].update(result[node])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    # add to queue for processing
                    dq.append(neighbor)
        return [sorted(s) for s in result]


class Solution1:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = [set() for _ in range(n)]
        graph = defaultdict(list)
        in_degrees = [0] * n
        for u,v in edges:
            result[v].add(u)
            graph[u].append(v)
            in_degrees[v] += 1
        queue = [node for node, degree in enumerate(in_degrees) if degree == 0]
        while queue:
            node = queue.pop(0)
            for nei in graph[node]:
                result[nei].update(result[node])
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    queue.append(nei)       
        return [sorted(s) for s in result]
        

            

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(Solution().getAncestors(
    n=n, edges=edgeList)==[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]])

n = 5
edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().getAncestors(
    n=n, edges=edgeList)==[[],[0],[0,1],[0,1,2],[0,1,2,3]])

n = 6
edgeList = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]
print(Solution().getAncestors(
    n=n, edges=edgeList)==[[2,4,5],[0,2,4,5],[4],[0,1,2,4,5],[],[2,4]])