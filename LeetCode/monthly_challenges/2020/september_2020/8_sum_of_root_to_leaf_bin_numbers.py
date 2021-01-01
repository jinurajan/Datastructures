"""
1022. Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return int(str(root.val), 2)
        paths = []
        temp = ""
        self.find_paths(root, paths, temp)
        return sum([int(i, 2) for i in paths])

    def find_paths(self, root, paths, temp):
        if not root:
            return
        if root.left is None and root.right is None:
            temp += str(root.val)
            paths.append(temp)
            return
        temp += str(root.val)
        self.find_paths(root.left, paths, temp)
        self.find_paths(root.right, paths, temp)


class Solution1(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        return self.eval_sum(root, 0)

    def eval_sum(self, root, total_sum):
        if not root.left and not root.right:
            return total_sum*2 + root.val
        elif not root.left:
            return self.eval_sum(root.right, total_sum * 2 + root.val)
        elif not root.right:
            return self.eval_sum(root.left, total_sum * 2 + root.val)
        else:
            return self.eval_sum(root.left, total_sum * 2 + root.val) + \
                self.eval_sum(root.right, total_sum * 2 + root.val)



root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print Solution().sumRootToLeaf(root)
print Solution().sumRootToLeaf(None)
print Solution().sumRootToLeaf(TreeNode(1))

print Solution1().sumRootToLeaf(root)
print Solution1().sumRootToLeaf(None)
print Solution1().sumRootToLeaf(TreeNode(1))
