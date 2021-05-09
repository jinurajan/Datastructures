"""
Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False

        def is_equal(root_1, root_2):
            if not root_1 and not root_2:
                return True
            if not root_1 or not root_2:
                return False
            if root_1.val != root_2.val:
                return False

            return is_equal(root_1.left, root_2.left) and is_equal(root_1.right, root_2.right)

        if is_equal(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return '^' + str(p.val) + convert(p.left) + convert(p.right) if p else '$'

        return convert(t) in convert(s)