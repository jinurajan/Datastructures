"""
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Q = [root]
        result = []
        while Q:
            level_nodes = []
            size = len(Q)
            while size:
                node = Q.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                size -= 1
            result.append(level_nodes)
        return result



from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        result = []
        while Q:
            level_nodes = []
            size = len(Q)
            while size:
                node = Q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                size -= 1
            result.append(level_nodes)
        return result


t = TreeNode(-10)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print(Solution().levelOrder(t))





