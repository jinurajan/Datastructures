"""
Given the root of a binary tree, the task is to flatten the tree into a linked list using the same TreeNode class. The left child pointer of each node in the linked list should always be NULL, and the right child pointer should point to the next node in the linked list. The nodes in the linked list should be in the same order as that of the preorder traversal of the given binary tree.

"""
from binary_tree import *
from binary_tree_node import *

def flatten_tree(root):
    if not root:
        return
    node = root
    while node:
        if node.left:
            last = node.left
            while last.right:
                last = last.right
            last.right = node.right
            node.right = node.left
            node.left = None
        node = node.right 
    return root