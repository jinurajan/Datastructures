"""
Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest, val = float("inf"), None
        def dfs(node, target):
            nonlocal closest, val
            if not node:
                return
            if closest > abs(node.val-target):
                closest = abs(node.val-target):
                val = node.val
            if node.val > target:
                dfs(node.left, target)
            else:
                dfs(node.right, target)
        dfs(root, target)
        return val
