"""
Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        def is_symmetric(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return is_symmetric(root1.left, root2.right) and is_symmetric(root1.right, root2.left)
        return is_symmetric(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        q = []
        q.append(root.left)
        q.append(root.right)
        while q:
            r1 = q.pop()
            r2 = q.pop()
            if not r1 and not r2:
                continue
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            q.append(r1.left)
            q.append(r2.right)
            q.append(r1.right)
            q.append(r2.left)
        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(3)
root.right.left = TreeNode(4)
print(Solution().isSymmetric(root))
