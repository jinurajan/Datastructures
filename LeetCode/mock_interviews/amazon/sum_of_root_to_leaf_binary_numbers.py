"""
Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
Example 3:

Input: root = [1]
Output: 1
Example 4:

Input: root = [1,1]
Output: 3


Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        paths = []
        temp = ""
        self.find_paths(root, paths, temp)
        return sum([int(i, 2) for i in paths])

    def find_paths(self, root, paths, temp):
        if not root:
            return
        if root.left is None and root.right is None:
            temp += str(root.val)
            paths.append(temp)
            return
        temp += str(root.val)
        self.find_paths(root.left, paths, temp)
        self.find_paths(root.right, paths, temp)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        path = []

        def dfs(node, path):
            if node:
                path.append(str(node.val))
            if not node.left and not node.right:
                result.append("".join(path[:]))
                return
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()

        dfs(root, path)
        return sum([int(binary, 2) for binary in result])









