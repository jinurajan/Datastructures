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
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        self.val = float("-inf")
        def inorder(node):
            if not node:
                return True
            ll = inorder(node.left)
            # reached left most
            if node.val <= self.val:
                return False
            self.val = node.val
            rl = inorder(node.right)
            return ll and rl

        bl = inorder(root)
        return bl