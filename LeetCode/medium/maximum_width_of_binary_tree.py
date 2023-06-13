"""
Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        do a bfs and count the width and update. also consider adding null
        """
        if not root:
            return 0
        max_width = 0
        q = [(root, 0)]
        while q:
            l = len(q)
            _, level = q[0]
            for i in range(l):
                node, col_level = q.pop(0)
                if node.left:
                    q.append((node.left, 2*col_level))
                if node.right:
                    q.append((node.right, 2*col_level+1))
            max_width = max(max_width, col_level-level+1)
        return max_width


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        first_col_index_map = {}

        def dfs(node, depth, col_index):
            nonlocal max_width
            if not node:
                return
            if depth not in first_col_index_map:
                first_col_index_map[depth] = col_index

            max_width = max(max_width, col_index-first_col_index_map[depth]+1)

            dfs(node.left, depth+1, 2*col_index)
            dfs(node.right, depth+1, 2*col_index+1)

        dfs(root, 0, 0)
        return max_width


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        do a bfs and count the width and update. also consider adding null
        """
        if not root:
            return 0
        max_width = 0
        q = [(root, 0)]
        while q:
            l = len(q)
            _, level = q[0]
            first, last = 0, 0 
            for i in range(l):
                node, col_level = q.pop(0)
                curr_id = col_level - level
                if i == 0:
                    first = curr_id
                if i == l-1:
                    last = curr_id
                if node.left:
                    q.append((node.left, 2*col_level))
                if node.right:
                    q.append((node.right, 2*col_level+1))
            max_width = max(max_width, last-first+1)
        return max_width