"""
Cousins in Binary Tree

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level_parent_map = {}
        
        queue = [(root, 0, None)]
        x_visited = False
        y_visited = False
        while queue:
            l = len(queue)
            if x_visited and y_visited:
                break
            for i in range(l):
                node, level,parent = queue.pop(0)
                level_parent_map[node.val] = (level, parent)
                if node.left:
                    queue.append((node.left, level+1, node))
                if node.right:
                    queue.append((node.right, level+1, node))
                if node == x:
                    x_visited = True
                if node == y:
                    y_visited = True
        return level_parent_map[x][0] == level_parent_map[y][0] and    level_parent_map[x][1] != level_parent_map[y][1]   
        