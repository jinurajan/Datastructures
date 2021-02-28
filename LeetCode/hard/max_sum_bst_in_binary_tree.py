"""
Maximum Sum BST in Binary Tree

Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
Input: root = [2,1,3]
Output: 6
Input: root = [5,4,8,3,null,6,3]
Output: 7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = [0]
        max_val = float("inf")
        min_val = float("-inf")
        def dfs(node):
            if not node:
                return 0, True, min_val, max_val
            s1, bst1, max_1, min_1 = dfs(node.left)
            s2, bst2, max_2, min_2 = dfs(node.right)
            if bst1 and bst2 and max_1 < node.val < min_2:
                v = node.val + s1 + s2
                res[0] = max(res[0], v)
                return v, True, max(max_2, node.val), min(node.val, min_1)
            return 0, False, min_val, max_val
        dfs(root)
        return res[0]


root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(6)

print(Solution().maxSumBST(root))
