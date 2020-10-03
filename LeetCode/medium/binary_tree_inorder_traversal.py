"""
Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
        result = []
        inorder(root, result)
        return result
        
from collections import deque

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        q = deque()
        node = root
        while q or node:
            while node:
                q.append(node)
                node = node.left
            node = q.pop()
            result.append(node.val)
            node = node.right
        return result


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().inorderTraversal(root))


