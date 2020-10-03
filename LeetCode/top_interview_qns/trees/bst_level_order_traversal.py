"""
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

from collections import deque

class Solutio1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        q = deque([root, None])
        result = []
        level = []
        while q:
            print(q, level)
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                result.append(level)
                if len(q) >= 1:
                    q.append(None)
                level = []

        return result


class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        q = deque()
        q.append(root)
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
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        for i in range(1, h+1):
            res = []
            get_given_level(root, i, res)
            result.append(res)
        return result

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(Solution1().levelOrder(root))




# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print(Solution1().levelOrder(root))

# print("**********")

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(Solution().levelOrder(root))




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().levelOrder(root))

