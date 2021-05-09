"""
Two Sum BSTs

Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        visited = set()

        def search(node, target):
            if target in visited:
                return True
            if not node:
                return False
            if node.val == target:
                return True
            visited.add(node.val)
            if target >= node.val:
                return search(node.right, target)
            if target < node.val:
                return search(node.left, target)

        def traverse(node, t):
            if not node:
                return False
            if search(root2, t - node.val):
                return True
            return traverse(node.left, t) or traverse(node.right, t)

        return traverse(root1, target)


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        def fn(node):
            """Return inorder traversal of binary tree."""
            ans, stack = [], []
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    ans.append(node.val)
                    node = node.right
            return ans

        val1, val2 = fn(root1), fn(root2)
        lo, hi = 0, len(val2) - 1
        while lo < len(val1) and 0 <= hi:
            if val1[lo] + val2[hi] < target:
                lo += 1
            elif val1[lo] + val2[hi] == target:
                return True
            else:
                hi -= 1
        return False