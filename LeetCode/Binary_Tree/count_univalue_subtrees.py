"""
Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Input: root = [5,1,5,5,5,null,5]
Output: 4

Input: root = []
Output: 0

Input: root = [5,5,5,5,5,null,5]
Output: 6

Constraints:

The numbrt of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node):
            nonlocal max_count
            if not node.left and not node.right:
                max_count += 1
                return True
            is_uni = True
            if node.left:
                is_uni = dfs(node.left) and node.left.val == node.val and is_uni
            if node.right:
                is_uni = dfs(node.right) and node.right.val == node.val and is_uni
            max_count += is_uni
            return is_uni

        max_count = 0
        dfs(root)
        return max_count



t = TreeNode(5)
t.left = TreeNode(1)
t.left.left = TreeNode(5)
t.left.right = TreeNode(5)
t.right = TreeNode(5)
t.right.right = TreeNode(5)
import pdb; pdb.set_trace()
print(Solution().countUnivalSubtrees(t))