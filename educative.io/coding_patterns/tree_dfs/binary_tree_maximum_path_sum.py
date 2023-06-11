"""
Given the root of a binary tree, return the maximum sum of any non-empty path.

A path in a binary tree is defined as follows:

A sequence of nodes in which each pair of adjacent nodes must have an edge connecting them.
- A node can only be included in a path once at most.
- Including the root in the path is not compulsory.

You can calculate the path sum by adding up all node values in the path. To solve this problem, calculate the maximum path sum given the root of a binary tree so that there won’t be any greater path than it in the tree
"""


class MaxTreePathSum:
    def __init__(self):
        self.max_sum = float('-inf')

    def max_path_sum(self, root):
        self.max_contrib(root)
        return self.max_sum
    
    def max_contrib(self, root):
        if not root:
            return 0
        l_sum = max(self.max_contrib(root.left), 0)
        r_sum = max(self.max_contrib(root.right), 0)
        comb_sum = l_sum + r_sum + root.data
        self.max_sum = max(self.max_sum, comb_sum)
        return root.data + max(l_sum, r_sum)

        