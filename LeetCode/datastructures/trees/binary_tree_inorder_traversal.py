"""
Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
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
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
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


class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        result = []
        def inorder(node, r):
            if not node:
                return
            inorder(node.left, r)
            r.append(node.val)
            inorder(node.right, r)

        inorder(root, result)
        return result


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        s = []
        node = root
        while True:
            if node:
                s.append(node)
                node = node.left
            else:
                if not s:
                    break
                node = s.pop(-1)
                result.append(node.val)
                node = node.right
    
        return result



root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
print(Solution1().inorderTraversal(root))
print(Solution().inorderTraversal(root))


