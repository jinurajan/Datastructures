"""
783. Minimum Distance Between BST Nodes
Easy
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
from sys import maxint


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_min_diff(node):
            if node:
                l_min, l_max, l_diff = find_min_diff(node.left)
                r_min, r_max, r_diff = find_min_diff(node.right)
                diff = min(l_diff, r_diff, abs(node.val - l_max), abs(node.val - r_min))
                min_val = min(l_min, node.val)
                max_val = max(r_max, node.val)
                return min_val, max_val, diff
            return maxint, -maxint, maxint

        min_val, max_val, diff = find_min_diff(root)
        return diff

                

class Solution1(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
       


# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# print Solution().minDiffInBST(root)


# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(48)
# root.right.left = TreeNode(12)
# root.right.right = TreeNode(49)
# print Solution().minDiffInBST(root)


root = TreeNode(90)
root.left = TreeNode(69)
root.left.right = TreeNode(89)
root.left.left = TreeNode(49)
root.left.left.right = TreeNode(52)
print Solution().minDiffInBST(root)


        
