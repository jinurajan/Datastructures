"""
Delete Leaves With a Given Value

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).



Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Example 4:

Input: root = [1,1,1], target = 1
Output: []
Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]


Constraints:

1 <= target <= 1000
The given binary tree will have between 1 and 3000 nodes.
Each node's value is between [1, 1000].
"""


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        count = 0

        def remove_leafs_with_target(node):
            nonlocal count
            if not node:
                return None
            if not node.left and not node.right:
                if node.val == target:
                    count += 1
                    return None
                return node

            node.left = remove_leafs_with_target(node.left)
            node.right = remove_leafs_with_target(node.right)
            return node

        new_root = remove_leafs_with_target(root)
        while count > 0:
            count = 0
            new_root = remove_leafs_with_target(new_root)
        return new_root




