"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:

The binary tree will have at most 200 nodes.
The value of each node will only be 0 or 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(node, sum_val):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            l = dfs(node.left, sum_val)
            r = dfs(node.right, sum_val)
            if not l:
                node.left = None
            if not r:
                node.right = None
            return l + r + node.val

        dfs(root, 0)
        if not root.left and not root.right and not root.val:
            root = None
        return root
