"""
Most Frequent Subtree Sum
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        def find_subtree_sum(node):
            if not node:
                return 0
            ans = find_subtree_sum(node.left) + find_subtree_sum(node.right)
            frequency_hash[ans] = frequency_hash.get(ans, 0) + 1
            return ans

        frequency_hash = {}
        find_subtree_sum(root)
        max_freq = max(frequency_hash.values())
        result = []
        for key, val in frequency_hash.items():
            if val == max_freq:
                result.append(key)
        return result