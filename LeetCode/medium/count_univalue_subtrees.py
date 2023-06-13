"""
Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value 
subtrees
.

A uni-value subtree means all nodes of the subtree have the same value.

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node.left and not node.right:
                count += 1
                return True
            is_uni = True
            if node.left:
                is_uni = dfs(node.left) and node.left.val == node.val and is_uni
            if node.right:
                is_uni = dfs(node.right) and node.right.val == node.val and is_uni
            
            count += is_uni
            return is_uni
        
        dfs(root)
        return count