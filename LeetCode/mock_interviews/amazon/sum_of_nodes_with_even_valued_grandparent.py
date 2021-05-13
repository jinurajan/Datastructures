"""
Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, None, None)]
        sum_val = 0
        def dfs(node, parent, grand_parent):
            nonlocal sum_val
            if not node:
                return
            if grand_parent and grand_parent.val % 2 == 0:
                sum_val += node.val
            if node.left:
                dfs(node.left, node, parent)
            if node.right:
                dfs(node.right, node, parent)
        dfs(root, None, None)
        return sum_val

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, None, None)]
        sum_val = 0
        while q:
            l = len(q)
            node, parent, gp = q.pop()
            if node.left:
                q.append((node.left, node, parent))
            if node.right:
                q.append((node.right, node, parent))
            if gp and gp.val % 2 == 0:
                sum_val += node.val
        return sum_val

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, None, None)]
        sum_val = 0
        while q:
            l = len(q)
            for i in range(l):
                node, parent, gp = q.pop(0)
                if node.left:
                    q.append((node.left, node, parent))
                if node.right:
                    q.append((node.right, node, parent))
                if gp and gp.val % 2 == 0:
                    sum_val += node.val
        return sum_val
