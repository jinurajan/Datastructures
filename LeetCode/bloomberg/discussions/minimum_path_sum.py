"""
Binary Tree Minimum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the minimum path sum of any path.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""

class Solution:
    def minPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = root.val
        if not root.left and not root.right:
            return sum
        else:
            left_sum = min(self.minPathSum(root.left), float("inf"))
            right_sum = min(self.minPathSum(root.right), float("inf"))

        if left_sum > right_sum:
            sum += left_sum
        else:
            sum += right_sum

        return sum