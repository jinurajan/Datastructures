"""
 Find a Corresponding Node of a Binary Tree in a Clone of That Tree
 Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:

Input: tree = [7], target =  7
Output: 7

Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5

Input: tree = [1,2,null,3], target = 2
Output: 2

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        result = [None]
        def find_node(node, target, result):
            if not node:
                # null return
                return
            if node.val == target.val:
                result[0] = node
                return
            find_node(node.left, target, result)
            find_node(node.right, target, result)

        find_node(cloned, target, result)
        return result[0]


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        reference = self.getTargetCopy(original.left, cloned.left, target)
        if reference:
            return reference
        return self.getTargetCopy(original.right, cloned.right, target)


root1 = TreeNode(7)
root1.left = TreeNode(4)
root1.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(19)


root2 = TreeNode(7)
root2.left = TreeNode(4)
root2.right = TreeNode(3)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(19)


print(Solution().getTargetCopy(root1, root2, root1.right).val)
