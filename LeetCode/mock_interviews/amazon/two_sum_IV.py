"""
Two Sum IV - Input is a BST
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Input: root = [2,1,3], k = 4
Output: true

Input: root = [2,1,3], k = 1
Output: false

Input: root = [2,1,3], k = 3
Output: true

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root or (not root.left and not root.right):
            return False
        queue = deque([root])
        visited = set()
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if k - node.val in visited:
                    return True
                visited.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodeset = set()

        def traverse(node, k, nodeset):
            if not node:
                return False
            if k - node.val in nodeset:
                return True
            nodeset.add(node.val)
            return traverse(node.left, k, nodeset) or traverse(node.right, k, nodeset)

        return traverse(root, k, nodeset)

