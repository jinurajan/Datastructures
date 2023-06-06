"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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