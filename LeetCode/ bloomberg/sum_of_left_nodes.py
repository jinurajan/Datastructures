"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, t):
            if not node:
                return 0
            if t == "left" and not node.left and not node.right:
                return node.val
            l_sum, r_sum = 0, 0
            if node.left:
                l_sum = dfs(node.left, "left")
            if node.right:
                r_sum = dfs(node.right, "right")
            return l_sum + r_sum
        
        return dfs(root, None)
        
        
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, None)]
        result = 0
        while queue:
            node, type = queue.pop(0)
            if type == "left":
                if not node.left and not node.right:
                    result += node.val
            if node.left:
                queue.append((node.left, "left"))
            if node.right:
                queue.append((node.right, "right"))
        
        return result