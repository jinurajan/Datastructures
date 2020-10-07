"""
Binary Tree Postorder Traversal


Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [2,1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        def post_order(node, r):
            if not node:
                return
            post_order(node.left, r)
            post_order(node.right, r)
            r.append(node.val)

        post_order(root, result)
        return result


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        node = root
        while True:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left

            node = stack.pop()
            if node.right and stack[-1] == node.right:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                result.append(node.val)
                node = None
            if len(stack) <= 0:
                break

        return result


root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
print(Solution1().postorderTraversal(root))
print(Solution().postorderTraversal(root))
