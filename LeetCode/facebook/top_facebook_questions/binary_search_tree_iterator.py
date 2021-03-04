"""
Binary Search Tree Iterator
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.


Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder_traversal = deque()
        self.inorder(root)

    def next(self) -> int:
        return self.inorder_traversal.popleft()

    def hasNext(self) -> bool:
        return len(self.inorder_traversal) > 0

    def inorder(self, node) -> None:
        if not node:
            return
        self.inorder(node.left)
        self.inorder_traversal.append(node.val)
        self.inorder(node.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.left_most_inorder(root)

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self.left_most_inorder(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def left_most_inorder(self, node) -> None:
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()