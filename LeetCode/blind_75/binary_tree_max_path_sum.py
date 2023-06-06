"""
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


four possibilities
- The path starts at the root and goes down through the root's left child. We don't know how long the path is, but it could extend to the bottom of the left subtree.
- The path starts at the root and goes down through the root's right child. Very similar to the previous case, but the direction is toward the right.
- The path involves both the left and the right child.
- The path doesn't involve any child. The root itself is the only element of the path with maximum sum.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def path_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            l_sum = max(path_sum(node.left), 0)
            r_sum = max(path_sum(node.right), 0)
            comb_sum = node.val + l_sum + r_sum
            max_sum = max(comb_sum, max_sum)
            return node.val + max(l_sum, r_sum)
        
        max_sum = float("-inf")
        path_sum(root)
        return max_sum

