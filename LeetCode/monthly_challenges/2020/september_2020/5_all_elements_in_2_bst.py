"""
All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        l1, l2 = [], []
        self.inorder_traversal(root1, l1)
        self.inorder_traversal(root2, l2)
        print l1, l2
        if not l1:
            return l2
        if not l2:
            return l1
        return self.merge(l1, l2)

    def merge(self, a1, a2):
        r = []
        i, j = 0, 0
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                r.append(a1[i])
                i += 1
            else:
                r.append(a2[j])
                j += 1
        print i, j
        if i < len(a1):
            # first array is left
            r.extend(a1[i:])
        elif j < len(a2):
            # second array is left
            r.extend(a2[j:])
        return r

    def inorder_traversal(self, root, r):
        if not root:
            return r
        self.inorder_traversal(root.left, r)
        r.append(root.val)
        self.inorder_traversal(root.right, r)
