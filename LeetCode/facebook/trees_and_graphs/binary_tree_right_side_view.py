"""
Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]

"""
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        Q = [root]
        while Q:
            size = len(Q)
            res.append(Q[-1].val)
            while size:
                node = Q.pop(0)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                size -= 1
        return res

t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(6)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)

print(Solution().rightSideView(t))
