"""
Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



thinking
1. connected undirected 
2. deepcopy 
3. each node has val and list of neighbour nodes

1.try bfs ?
2. avoid loops with visited

"""

"""

"""
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs
        if not node:
            return node
        q = deque([node])
        visited = {node: Node(node.val)}
        while q:
            n = q.popleft()
            for neigh in n.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    q.append(neigh)
                visited[n].neighbors.append(visited[neigh])        
        return visited[node]



class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dfs
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val)

        self.visited[node] = new_node
        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(neigh) for neigh in node.neighbors]
        return new_node


