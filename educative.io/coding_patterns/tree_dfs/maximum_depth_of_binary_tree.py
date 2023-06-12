"""
Given the root of a binary tree, return its maximum depth. A binary tree’s maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""


from binary_tree import *
from collections import deque

def max_depth(root):
    if not root:
        return 0
    l_depth = max_depth(root.left)
    r_depth = max_depth(root.right)

    return max(l_depth, r_depth) + 1

