"""
Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        q = deque([root])
        result = []
        while len(q) > 0:
            row =[]
            row_size = len(q)
            while row_size > 0:
                node = q.popleft()
                row.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                row_size -= 1
            result.insert(0, row)
        return result


class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        q = deque([root])
        result = []
        while len(q) > 0:
            row =[]
            row_size = len(q)
            while row_size > 0:
                node = q.popleft()
                row.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                row_size -= 1
            result.append(row)
        return result[::-1]


class Solution3:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]

        def get_height(node, height):
            if not node:
                return height
            elif not node.left and not node.right:
                return height + 1
            else:
                return max(get_height(node.left, height+1), get_height(node.right, height+1))

        def get_given_level(node, height, res):
            if not node:
                return res
            if height == 1:
                res.append(node.val)
            else:
                get_given_level(node.left, height-1, res)
                get_given_level(node.right, height-1, res)

        result = []
        h = get_height(root, 0)
        print(h)
        for i in range(h, 0, -1):
            res = []
            get_given_level(root, i, res)
            result.append(res)
        return result

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def traverse(node, level):
            if node:
                if level >= len(res):
                    res.append([])
                traverse(node.left, level+1)
                traverse(node.right, level+1)
                res[level].append(node.val)

        res = []
        traverse(root, 0)
        return res[::-1]





root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrderBottom(root))