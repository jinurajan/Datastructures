"""
Graph Valid Tree


You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

1. There are no self-loops or repeated edges.
2. 1 <= n <= 2000
3. 0 <= edges.length <= 5000
4. edges[i].length == 2
5. 0 <= ai, bi < n
6. ai != bi

thoughts
1. G is fully connected. each node should be reachable. ie if we do dfs we should visit all nodes
2. G contains no cycle. if dfs does not encounter already visited node
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs
        if len(edges) != n-1:
            return False
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        parent = {0: -1}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                stack.append(neighbour)
        return len(parent) == n

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # recursive dfs
        if len(edges) != n-1:
            return False
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                result = dfs(neighbour, node)
                if not result:
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)
        return len(visited) == n

class UnionFind:
    
    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n
        
    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, A):
        # Step 1: Find the root.
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        # Step 2: Do a second traversal, this time setting each node to point
        # directly at A as we go.
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
        
    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Create a new UnionFind object with n nodes. 
        unionFind = UnionFind(n)
        
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        
        # If we got this far, there's no cycles!
        return True
