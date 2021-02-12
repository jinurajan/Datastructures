"""
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Input: root = []
Output: 0

Input: root = [0]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        """
        top down approach
        """
        if not root:
            return 0

        def depth(node, height):
            if not node:
                return height
            l_height = depth(node.left, height+1)
            r_height = depth(node.right, height+1)
            return max(l_height, r_height)
        return depth(root, 0)


class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        """
        top down approach
        """
        if not root:
            return 0
        l_height = self.maxDepth(root.left) + 1
        r_height = self.maxDepth(root.right) + 1
        return max(l_height, r_height)

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(5)
t.right.right = TreeNode(6)
t.right.right.right = TreeNode(7)
print(Solution1().maxDepth(t))
print(Solution2().maxDepth(t))