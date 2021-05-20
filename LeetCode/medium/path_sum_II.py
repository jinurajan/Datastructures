"""
Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Input: root = [1,2,3], targetSum = 5
Output: []

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        result = []
        path = []

        def dfs(node, path_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and path_sum == node.val:
                result.append(path[:])
            else:
                dfs(node.left, path_sum - node.val)
                dfs(node.right, path_sum - node.val)
            path.pop()

        dfs(root, targetSum)
        return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(node, path_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and path_sum + node.val == targetSum:
                result.append(path[:])
            else:
                dfs(node.left, path_sum + node.val)
                dfs(node.right, path_sum + node.val)
            path.pop()

        dfs(root, 0)
        return result





