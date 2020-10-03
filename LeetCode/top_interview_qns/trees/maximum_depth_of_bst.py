"""
Maximum Depth of Binary Tree

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
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def max_height(node, height):
            if node is None:
                return height
            elif root.left is None and root.right is None:
                return height + 1
            else:
                return max(max_height(node.left, height + 1), max_height(node.right, height + 1))
        return max_height(root, 0)