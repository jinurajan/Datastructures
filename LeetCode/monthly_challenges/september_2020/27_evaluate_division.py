"""
Evaluate Division

You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

 

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
1 <= equations[i][0], equations[i][1] <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0], queries[i][1] <= 5
equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.
"""
from collections import defaultdict
from itertools import chain

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        
        1. considering this as a graph we can perform dfs/bfs to to be able to visit all nodes and the weights accordingly
        a -> b weight is 2
        b -> a weight is 1/2

        create a map of this values {a: {b: 2}, b: {a: 1/2}} and so on

        self.edges = {a: {b: 2.0}, b:{a: 0.5, c: 3.0}, c:{b: 0.333}}
        self.weights -> {a: [-1, -1], b: [-1, -1], c: [-1, -1]}
        loop 1
            v = 0
            dfs('a', 0, 1)
            {a: [0, 1], b: [-1, -1], c: [-1, -1]}
            j = b weight 2.0 ({b: 2.0})  a -> b
            dfs('b', 0, 1/2.0)  b -> a, b -> c
                b -> a
                {a: [0, 1], b: [0, 0.5], c: [-1, -1]}
                b -> c
                {a: [0, 1], b: [0, 0.5], c: [0, 0.16666]}
            return

        comp = number of components
        w = weight 

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


print Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print Solution().calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])



