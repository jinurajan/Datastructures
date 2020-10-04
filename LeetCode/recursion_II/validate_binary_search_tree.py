"""
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        def is_valid_bst(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return is_valid_bst(node.left, min_val, node.val) and is_valid_bst(
            node.right, node.val, max_val)
        
        return is_valid_bst(root.left, float("-inf"), root.val) and is_valid_bst(
            root.right, root.val, float("inf"))


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



root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().isValidBST(root))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().isValidBST(root))

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(6)
print(Solution().isValidBST(root))

root = TreeNode(4)
print(Solution().isValidBST(root))

print(Solution().isValidBST(None))


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(Solution().isValidBST(root))
