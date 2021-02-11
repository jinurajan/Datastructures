"""
Binary Tree Maximum Path Sum


A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = max(path_sum(node.left), 0)
            right_sum = max(path_sum(node.right), 0)
            combination_sum = node.val + left_sum + right_sum
            max_sum = max(combination_sum, max_sum)
            return node.val + max(left_sum, right_sum)

        max_sum = float('-inf')
        path_sum(root)
        return max_sum


t = TreeNode(-10)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
import pdb; pdb.set_trace()
print(Solution().maxPathSum(t))
# #
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print(Solution().maxPathSum(t))


t = TreeNode(1)
t.left = TreeNode(-2)
t.right = TreeNode(3)

print(Solution().maxPathSum(t))

t = TreeNode(-2)
t.left = TreeNode(-1)
print(Solution().maxPathSum(t))

t = TreeNode(2)
t.left = TreeNode(-1)
t.right = TreeNode(-2)
print(Solution().maxPathSum(t))


