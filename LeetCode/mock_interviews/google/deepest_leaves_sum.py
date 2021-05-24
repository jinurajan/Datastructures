"""
Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        while q:
            l = len(q)
            tmp_sum = 0
            for i in range(l):
                node = q.pop(0)
                tmp_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return tmp_sum

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        next_level = deque([root])
        while next_level:
            curr_level = next_level
            next_level = deque()
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return sum([node.val for node in curr_level])



