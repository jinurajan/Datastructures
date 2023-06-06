"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def traverse(node, max_val, min_val):
            if not node:
               return True
            if min_val < node.val < max_val:
                return traverse(
                    node.left, node.val, min_val) and traverse(
                    node.right, max_val, node.val
                )
            return False
        
        max_val = pow(2, 31) # keep +1 here
        min_val = -pow(2, 31)-1 # keep -1 here

        return traverse(root.left, root.val, min_val) and traverse(root.right, max_val, root.val)
