"""
Binary Tree Preorder Traversal

"""


# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursion(object):
    def preorderTraversal(self, root, result=None):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not result:
            result = []
        if not root:
            return
        result.append(root.val)
        self.preorderTraversal(root.left, result)
        self.preorderTraversal(root.right, result)
        return result

class SolutionIteration(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [root]
        while root is not None:
        	result.append



root = TreeNode('F')
root.left = TreeNode('B')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.right = TreeNode('G')
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')
print Solution().preorderTraversal(root)