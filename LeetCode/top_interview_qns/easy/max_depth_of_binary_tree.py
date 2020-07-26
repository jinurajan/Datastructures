"""
    Maximum Depth of Binary Tree

Solution
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            ld = 1 + self.maxDepth(root.left)
            rd = 1 + self.maxDepth(root.right)
            return ld if ld > rd else rd


if __name__ == "__main__":
    tree = TreeNode(val=3)
    tree.left = TreeNode(val=9)
    tree.left.left = TreeNode(val=10)
    tree.left.left.left = TreeNode(val=11)
    tree.left.left.left.left = TreeNode(val=22)
    tree.right = TreeNode(val=20)
    tree.right.left = TreeNode(val=15)
    tree.right.right = TreeNode(val=7)
    tree.right.right.left = TreeNode(val=6)
    tree.right.right.left.left = TreeNode(val=8)
    tree.right.right.left.left.right = TreeNode(val=36)
    print Solution().maxDepth(tree)
