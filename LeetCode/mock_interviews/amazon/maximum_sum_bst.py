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

Constraints:

The given binary tree will have between 1 and 40000 nodes.
Each node's value is between [-4 * 10^4 , 4 * 10^4].

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        result = [0]
        max_val = float("inf")
        min_val = float("-inf")

        def dfs(node):
            if not node:
                return 0, True, min_val, max_val
            l_sum, valid_1, max_val_1, min_val_1 = dfs(node.left)
            r_sum, valid_2, max_val_2, min_val_2 = dfs(node.right)
            if valid_1 and valid_2 and (max_val_1 < node.val < min_val_2):
                sum_val = l_sum + node.val + r_sum
                result[0] = max(sum_val, result[0])
                return sum_val, True, max(max_val_2, node.val), min(node.val, min_val_1)
            return 0, False, min_val, max_val

        dfs(root)
        return result[0]