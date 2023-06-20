"""
Clone Binary Tree With Random Pointer

A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.
"""
from typing import Optional

# Definition for Node.
# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        """
        traverse each node and create a new node / link with existing node
        """
        node_map = {}
        
        def dfs(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            new_node = NodeCopy(node.val)
            node_map[node] = new_node

            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)
            new_node.random = dfs(node.random)
            return node_map[node]
        
        return dfs(root)
        
        

class Solution:
    
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        """
        traverse each node and create a new node / link with existing node
        """
        node_map = {}
        
        def dfs(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            new_node = NodeCopy(node.val)
            node_map[node] = new_node

            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)
            new_node.random = dfs(node.random)
            return node_map[node]
        
        return dfs(root)
        
        