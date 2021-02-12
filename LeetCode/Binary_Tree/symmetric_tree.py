"""
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

But the following [1,2,2,null,3,null,3] is not:

"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root])
        while q:
            l = len(q)
            level_nodes = []
            while l:
                node = q.popleft()
                if node:
                    level_nodes.append(node.val)
                else:
                    level_nodes.append(None)
                if node:
                    q.append(node.left)
                if node:
                    q.append(node.right)
                l -= 1
            if level_nodes != level_nodes[::-1]:
                return False
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_symmetric(l_node, r_node):
            if not l_node and not r_node:
                return True
            elif not l_node or not r_node:
                return False
            elif l_node.val != r_node.val:
                return False
            else:
                return is_symmetric(
                    l_node.left, r_node.right) and is_symmetric(
                    l_node.right, r_node.left)

        return is_symmetric(root.left, root.right)


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(5)
t.right.right = TreeNode(6)
#
print(Solution().isSymmetric(t))

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right = TreeNode(2)
t.right.right = TreeNode(3)
t.right.left = TreeNode(4)
import pdb; pdb.set_trace()
print(Solution().isSymmetric(t))

t = TreeNode(1)
t.left = TreeNode(2)
t.left.right = TreeNode(3)
t.right = TreeNode(2)
t.right.right = TreeNode(3)
print(Solution().isSymmetric(t))


