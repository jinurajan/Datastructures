"""
1042. Flower Planting With No Adjacent Easy
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
"""
from collections import defaultdict


class Solution2(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * (N + 1)   # for not colored
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(graph, node, result):
            if result[node] > 0:
                # already colored
                return True
            # get all used colord
            used = set([result[v] for v in graph[node] if result[v] > 0])
            if len(used) == 4:
                return False
            for i in range(1, 5):
                if i not in used:
                    # i is not been used yet
                    result[node] = i
                    isok = True
                    for v in graph[node]:
                        # all neighbours of node
                        if not dfs(graph, v, result):
                            # not colored yet
                            isok = False
                            break
                    if isok:
                        return True
            return False

        for node in range(1, N + 1):
            dfs(graph, node, result)
        return result[1:]


class Solution1(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = []
        flowers = [1, 2, 3, 4]
        visited = [0] * N
        path_set = {}
        for p in paths:
            if p[0] in path_set:
                path_set[p[0]].append(p[1])
            else:
                path_set[p[0]] = [p[1]]
        self.bfs(1, result, path_set, visited, flowers, N)
        return result

    def bfs(self, garden, result, path_set, visited, flowers, N):
        queue = []
        queue.append(garden)
        visited[garden - 1] = 1
        i = 0
        result.append(flowers[i])
        i += 1
        while queue:
            if len(result) == N:
                break
            if i == len(flowers):
                i = 0
            s = queue.pop(0)
            result.append(flowers[i])
            i += 1
            neighbours = path_set.get(s, [])
            for s in neighbours:
                if not visited[s - 1]:
                    queue.append(s)
                    result.append(flowers[i])
                    visited[s - 1] = 1
                    i += 1
        return result


class Solution3(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """  # for not colored
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        res = [1] * N
        for n in graph:
            col = [1, 2, 3, 4]
            for adj in graph[n]:
                if res[adj - 1] != 0 and res[adj - 1] in col:
                    col.remove(res[adj - 1])
            res[n - 1] = col[0]
        return res

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """  # for not colored
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        res = [0] * N
        for garden in range(1, N+1):
            colors = [1,2,3,4]
            if garden not in graph:
                # standing alone no neighbours
                res[garden - 1] = 1
            for neighbour in graph[garden]:
                neighbour_color = res[neighbour - 1]
                if neighbour_color and neighbour_color in colors:
                    colors.remove(neighbour_color)
            res[garden - 1] = colors[0]
        return res

# print Solution().gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]) == [1, 2, 3]
# print Solution().gardenNoAdj(4, [[1, 2], [3, 4]]) == [1, 2, 1, 2]
# print Solution().gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == [1, 2, 3, 4]
print Solution().gardenNoAdj(5, [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]) #[1, 2, 1, 3, 3]
