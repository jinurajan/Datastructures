"""
Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Input: root = [1,2]
Output: [2,1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up:

Recursive solution is trivial, could you do it iteratively?

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def post_order(node):
            if not node:
                return
            post_order(node.left)
            post_order(node.right)
            result.append(node.val)
        result = []
        post_order(root)
        return result

from collections import deque

class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        s = deque([root])
        result = []
        while s:
            node = s.pop()
            result.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return result[::-1]


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = deque()
        node = root
        last_popped = None
        result = []
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                top = s[-1]
                if top.right and top.right != last_popped:
                    node = top.right
                else:
                    last_popped = s.pop()
                    result.append(last_popped.val)
        return result


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(5)
t.right.right = TreeNode(6)
print(Solution().postorderTraversal(t))
print(Solution1().postorderTraversal(t))
print(Solution2().postorderTraversal(t))