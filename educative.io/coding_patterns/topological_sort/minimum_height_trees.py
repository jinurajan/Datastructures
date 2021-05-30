"""
Minimum Height Trees (hard) #
We are given an undirected graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

Example 1:

Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '1' or '2' is three which is minimum.


Note: Any node with one edge can be the root. eliminate from below all leaf nodes until we have one node with one edge which can be root
"""

from collections import defaultdict

def find_trees(nodes, edges):
    if not nodes:
        return []
    if nodes == 1:
        return [0]
    indegree ={i: 0 for i in range(nodes)}
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        indegree[v] += 1
        indegree[u] += 1
    leaves = [k for k, v in indegree.items() if v == 1]
    total_nodes = nodes
    while total_nodes > 2:
        l = len(leaves)
        total_nodes -= l
        for _ in range(l):
            node = leaves.pop(0)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    leaves.append(nei)
    return list(leaves)

def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()