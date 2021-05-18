"""
Maximum Average Subtree
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.


Note:

The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_avg = 0

        def dfs(node: TreeNode):
            nonlocal max_avg
            if not node:
                return 0, 0
            leftsum, n_left = dfs(node.left)
            rightsum, n_right = dfs(node.right)

            cur_sum = leftsum + rightsum + node.val
            cur_num_nodes = n_left + n_right + 1

            max_avg = max(max_avg, cur_sum / cur_num_nodes)
            return cur_sum, cur_num_nodes

        dfs(root)

        return max_avg


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:

        max_average = 0

        def dfs(node, node_count, value_sum):
            nonlocal max_average
            if not node:
                return 0, 0, 0
            if not node.left and not node.right:
                # leaf node
                return 1, node.val, node.val
            l_count, l_sum, l_avg = dfs(node.left, node_count, value_sum)
            r_count, r_sum, r_avg = dfs(node.right, node_count, value_sum)
            value_sum = l_sum + r_sum + node.val
            node_count = l_count + r_count + 1
            max_average = max(max_average, max(l_avg, r_avg, (value_sum / node_count)))
            return node_count, value_sum, value_sum / node_count

        dfs(root, 0, 0)

        return max_average
