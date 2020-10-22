"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n < 1:
            return None
        elif n == 1:
            return TreeNode(nums[0])
        else:
            mid = n // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root


class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def bst_helper(nums, l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            else:
                mid = (l + r) // 2
                node = TreeNode(nums[mid])
                node.left = bst_helper(nums, l, mid-1)
                node.right = bst_helper(nums, mid+1, r)
                return node
        return bst_helper(nums, 0, len(nums)-1)

class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        l, r = 0, len(nums)-1
        root = None
        import pdb; pdb.set_trace()
        stack = [root]
        while True:
            node = stack.pop(-1)
            mid = (l + r) // 2
            stack.append(nums[mid])
            if not root:
                val = stack.pop(-1)
                root = TreeNode(val)
                node = root
            if mid-1 >= 0:
                stack.append(nums[mid-1])
            if mid+1 < n:
                stack.append(nums[mid+1])
                l = mid + 1
            while len(stack) > 0:
                val = stack.pop()
                if val > node.val:
                    node.right = TreeNode(val)
                else:
                    node.left = TreeNode(val)
        return root



def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


root = Solution().sortedArrayToBST([1,2,3,4,5,6])
inorder(root)
print("")
root = Solution1().sortedArrayToBST([1,2,3,4,5,6])
inorder(root)

root = Solution1().sortedArrayToBST([1,2,3,4,5,6])
inorder(root)


