"""
Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def preorder(node, result):
            if not node:
                return
            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)

        result = []
        preorder(root, result)
        return result

from collections import deque

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        s = deque([root])
        result = []
        while s:
            node = s.pop()
            result.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return result







t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(5)
t.right.right = TreeNode(6)
print(Solution().preorderTraversal(t))




