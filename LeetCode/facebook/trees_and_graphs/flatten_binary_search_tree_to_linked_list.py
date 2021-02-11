"""
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Input: root = []
Output: []

Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


def print_l(node):
    if not node:
        return
    print(node.val, end="->")
    print_l(node.right)


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(5)
t.right.right = TreeNode(6)
import pdb;pdb.set_trace()
Solution().flatten(t)
print_l(t)



