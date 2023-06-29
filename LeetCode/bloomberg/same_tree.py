"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            n1 = node1.val if node1 else None
            n2 = node2.val if node2 else None
            if n1 == n2:
                return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
            else:
                return False
        
        return traverse(p, q)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        traverse each node and if it is not equal return
        if both are none return True else False
        """
        
        def is_equal(root_1, root_2):
            if not root_1 and not root_2:
                return True
            if not root_1 or not root_2:
                return False
            if root_1.val != root_2.val:
                return False
            return is_equal(root_1.left, root_2.left) and is_equal(root_1.right, root_2.right)
        
        return is_equal(p, q)
Console
