"""
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_path = 0
        def find_dia(node):
            nonlocal max_path
            if not node:
                return 0
            l_path = find_dia(node.left)
            r_path = find_dia(node.right)
            max_path = max(l_path+r_path+1, max_path)
            return max(l_path, r_path) + 1
        find_dia(root)
        return max_path -1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(10)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(8)
root.left.left.left.left = TreeNode(7)
root.left.right = TreeNode(5)
print(Solution().diameterOfBinaryTree(root))
