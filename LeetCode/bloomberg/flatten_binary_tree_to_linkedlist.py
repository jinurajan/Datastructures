"""
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        node = root
        while node:
            if node.left:
                last = node.left
                while last.right:
                    last = last.right

                last.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
        return root

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node):
            if not node or (not node.left and not node.right):
                return node
            left = flatten_tree(node.left)
            right = flatten_tree(node.right)
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            return right if right else left

        flatten_tree(root)