"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Input: preorder = [-1], inorder = [-1]
Output: [-1]

preorder is RootLeftRight

inorder is Left Root Right


first element in preorder is root

split the inorder you will get left subtree values and right subtree values

iteratively choose the next element in preorder to be the next parent value - left and iteratively use the left subtree

next one in preorder would be the right parent value and iteratively use the left subtree

using index_map would only work if there are no duplicate numbers. if it is a binary search tree we should use binarysearch to find the element and find the left and right subtree from there


"""
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_val]-1)
            root.right = array_to_tree(inorder_index_map[root_val]+1, right)

            return root
        
        # first element is the root in preorder
        preorder_index = 0
        inorder_index_map ={}
        for idx, val in enumerate(inorder):
            # wont work if there is duplicate numbers in tree
            inorder_index_map[val] = idx
        
        return array_to_tree(0, len(preorder)-1)