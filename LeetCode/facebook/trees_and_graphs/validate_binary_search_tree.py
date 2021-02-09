"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = -1 * (pow(2, 31)+1)
        max_val = pow(2, 31)
        if not root.left and not root.right:
            return True
        def helper(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

        return helper(root, min_val, max_val)


t1 = TreeNode(2)
print(Solution().isValidBST(t1))

t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)
print(Solution().isValidBST(t1))


t1 = TreeNode(5)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.right.left = TreeNode(3)
t1.right.right = TreeNode(6)
print(Solution().isValidBST(t1))

t1 = TreeNode(1)
t1.left = TreeNode(1)
print(Solution().isValidBST(t1))

t1 = TreeNode(-2147483648)
t1.right = TreeNode(2147483647)
import pdb; pdb.set_trace()
print(Solution().isValidBST(t1))



