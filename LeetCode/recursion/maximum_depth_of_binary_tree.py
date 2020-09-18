"""
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        q = [3]  h =0
        loop 1 (while):
            nodes = 1
            h = 1
            while nodes > 0: loop1.1
                node = 3 q = []
                q = [9, 20]
                nodes = 0
        loop 2 (while):
            nodes = 2
            h = 2
            while nodes > 0 loop 2.1
                node = 9, q [20]
                nodes = 1

            while nodes > 0 loop 2.2
                node = 20 q = []
                q = [15, 7]
                nodes = 0
        loop 3 (while)
            nodes = 2
            h = 3
            while nodes > 0 loop 3.1
                node = 15 q [7]
                nodes = 1

            while nodes > 0 loop 3.2
                node = 7 q []
                nodes = 0

        loop 4 (while)
            nodes = 0
            return h
        """
        if root is None:
            return 0

        q = []
        q.append(root)
        height = 0
        while True:
            nodes = len(q)
            if nodes == 0:
                return height
            height += 1
            while nodes > 0:
                node = q[0]
                q.pop(0)
                if node.left:
                    q.append(node.left)
                if not node.right:
                    q.append(node.right)
                nodes -= 1


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node):
            if not node:
                return 0
            l_depth = 1 + depth(node.left)
            r_depth = 1 + depth(node.right)
            return l_depth if l_depth > r_depth else r_depth

        return depth(root)

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l_depth = 1 + self.maxDepth(root.left)
        r_depth = 1 + self.maxDepth(root.right)
        return l_depth if l_depth > r_depth else r_depth

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def max_height(node, height):
            if node is None:
                return height
            elif root.left is None and root.right is None:
                return height + 1
            else:
                return max(max_height(node.left, height + 1), max_height(node.right, height + 1))
        return max_height(root, 0)





root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

print Solution().maxDepth(root)
print Solution2().maxDepth(root)

root = TreeNode(1)
root.left = TreeNode(2)
print Solution().maxDepth(root)
print Solution1().maxDepth(root)





