"""
Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]

Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]

Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None

        def dfs(node, target):
            if not node:
                return None
            if not node.left and not node.right:
                # leaf node
                return None if target + node.val < limit else node
            node.left = dfs(node.left, target + node.val)
            node.right = dfs(node.right, target + node.val)

            return None if not node.left and not node.right else node

        return None if not dfs(root, 0) else root

