"""
Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves.

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        next_level = deque([root])
        while next_level:
            curr_level = next_level
            next_level = deque()
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return sum([node.val for node in curr_level])
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        q = [root]
        while q:
            n = len(q)
            level_nodes = deepcopy(q)
            print(level_nodes)
            while n > 0:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1

        return sum([node.val for node in level_nodes])


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        def depth(node, d):
            if not node:
                return d
            l_depth = depth(node.left, d) + 1
            r_depth = depth(node.right, d) + 1
            return l_depth if l_depth > r_depth else r_depth
        last_level_nodes = []
        def dfs(node, depth, max_depth):
            if depth == max_depth:
                last_level_nodes.append(node.val)
                return
            if node.left:
                dfs(node.left, depth+1, max_depth)
            if node.right:
                dfs(node.right, depth+1, max_depth)

        dfs(root, 1, depth(root, 0))
        return sum(last_level_nodes)



root = TreeNode(50)
root.right = TreeNode(54)
root.right.left = TreeNode(98)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(34)
print(Solution().deepestLeavesSum(root))