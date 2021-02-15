"""
Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def traverse(node, path):
            if not node:
                return
            if not node.left and not node.right:
                path += f"{node.val}"
                res.append(path)
                return
            else:
                path += f"{node.val}->"
            traverse(node.left, path)
            traverse(node.right, path)
        res = []
        traverse(root, "")
        return res

t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(6)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)

print(Solution().binaryTreePaths(t))