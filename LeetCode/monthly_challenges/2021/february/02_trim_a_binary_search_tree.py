"""
Trim a Binary Search Tree
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Input: root = [1], low = 1, high = 2
Output: [1]

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Input: root = [1,null,2], low = 2, high = 4
Output: [2]

Constraints:

The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
       """
       Inorder to analyze current node we need keep track of the parent node
       """
       def helper(current_node):
           if not current_node:
               return None
           current_node.left = helper(current_node.left)
           current_node.right = helper(current_node.right)
           if current_node.val < low:
               return current_node.right
           if current_node.val > high:
               return  current_node.left

           return current_node
       return helper(root)

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root




def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end='->')
    inorder(root.right)


t = TreeNode(3)
t.left = TreeNode(0)
t.right = TreeNode(4)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(1)

inorder(t)
# import pdb; pdb.set_trace()
t1 = Solution().trimBST(t, 1, 3)
inorder(t1)

