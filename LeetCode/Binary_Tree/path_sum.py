"""
Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [1,2], targetSum = 0
Output: false

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val)


r = TreeNode(2)
r.left = TreeNode(1)
r.right = TreeNode(4)
r.right.left = TreeNode(3)
r.right.right = TreeNode(5)
print(Solution().hasPathSum(r, 9))
print(Solution().hasPathSum(r, 10))
print(Solution().hasPathSum(r, 11))
print(Solution().hasPathSum(r, 1))
print(Solution().hasPathSum(r, 3))


r = TreeNode(1)
r.left = TreeNode(2)
print(Solution().hasPathSum(r, 1))

r = TreeNode(-2)
r.right = TreeNode(-3)
# import pdb; pdb.set_trace()
print(Solution().hasPathSum(r, -5))





