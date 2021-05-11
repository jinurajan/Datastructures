"""
Boundary of Binary Tree
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        leavenodes = []

        def leaves(root):
            if not root: return
            if not root.left and not root.right:
                leavenodes.append(root.val)
            leaves(root.left)
            leaves(root.right)

        leftnode = []
        # make sure to check whether the root is a leaf node or not
        if root.left or root.right:
            leftnode.append(root.val)

        def leftnodes(root):
            if not root: return
            if not root.left and not root.right: return
            if root:
                leftnode.append(root.val)
            if root.left:
                leftnodes(root.left)
            elif root.right:
                leftnodes(root.right)

        rightnode = []

        def rightnodes(root):
            if not root: return
            if not root.left and not root.right: return
            if root.right:
                rightnodes(root.right)
            elif root.left:
                rightnodes(root.left)
            rightnode.append(root.val)

        leaves(root)
        leftnodes(root.left)
        rightnodes(root.right)
        return leftnode + leavenodes + rightnode