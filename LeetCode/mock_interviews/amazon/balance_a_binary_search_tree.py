"""
Balance a Binary Search Tree
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        def inorder_search(node):
            if not node:
                return
            inorder_search(node.left)
            values.append(node.val)
            inorder_search(node.right)

        inorder_search(root)

        def bin_search(values, left, right):
            if left <= right:
                mid = left + (right - left) // 2
                curr = TreeNode(values[mid])
                curr.left = bin_search(values, left, mid - 1)
                curr.right = bin_search(values, mid + 1, right)
                return curr

        return bin_search(values, 0, len(values) - 1)



