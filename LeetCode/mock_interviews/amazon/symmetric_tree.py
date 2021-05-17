"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.issym(root.left, root.right)
    def issym(self, left, right):
        if not right or not left:
            return right == left
        elif left.val != right.val:
            return False
        return self.issym(left.left, right.right) and self.issym(left.right, right.left)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        def is_symmetric(root_1, root_2):
            if not root_1 and not root_2:
                return True
            if not root_1 or not root_2:
                return False
            if root_1.val != root_2.val:
                return False
            return is_symmetric(root_1.left, root_2.right) and is_symmetric(
                root_1.right, root_2.left)

        return is_symmetric(root.left, root.right)

