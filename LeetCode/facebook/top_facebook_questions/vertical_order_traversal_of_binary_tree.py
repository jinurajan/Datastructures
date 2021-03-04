"""
Vertical Order Traversal of a Binary Tree
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque, OrderedDict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        level_order_map = defaultdict(list)
        q = deque([(root, 0, 0)])
        node_list = []
        while q:
            node, row, col = q.popleft()
            if node:
                node_list.append((col, row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))
        node_list.sort()
        result = OrderedDict()
        for col, row, val in node_list:
            if col in result:
                result[col].append(val)
            else:
                result[col] = [val]
        return result.values()



