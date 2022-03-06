

from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_graph = defaultdict(list)
        for u,v in edges:
            in_graph[v].append(u)
        result_set = defaultdict(set)
        def dfs(node, ancestors):
            for neighbour in in_graph[node]:
                if result_set[neighbour]:
                    ancestors.update(result_set[neighbour])
                else:
                    ancestors.add(neighbour)
                dfs(neighbour, ancestors)
        result = []
        for i in range(n):
            ancestors = set()
            dfs(i, ancestors)
            result.append(sorted(ancestors))
        return result

            

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