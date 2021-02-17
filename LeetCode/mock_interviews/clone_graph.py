"""
Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        new_base_node = None
        S = deque([node])
        while S:
            node = S.pop()
            if node not in visited:
                new_node = Node(node.val)
                visited[node] = new_node
                if not new_base_node:
                    new_base_node = new_node
            else:
                new_node = visited[node]
            for n in node.neighbors:
                if n not in visited:
                    new_n = Node(n.val)
                    new_node.neighbors.append(new_n)
                    visited[n] = new_n
                    S.append(n)
                else:
                    new_node.neighbors.append(visited[n])
        return new_base_node