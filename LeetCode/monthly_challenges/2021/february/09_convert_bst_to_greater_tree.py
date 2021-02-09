"""
Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/



Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


Input: root = [0,null,1]
Output: [1,null,1]

Input: root = [1,0,2]
Output: [3,3,2]

Input: root = [3,2,4,1]
Output: [7,9,4,10]

Constraints:

The number of nodes in the tree is in the range [0, 104].
-104 <= Node.val <= 104
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.

"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution2:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root

class Solution1:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        if not root:
            return root
        node = root
        s = deque()
        while s or node:
            while node:
                s.append(node)
                node = node.right
            node = s.pop()
            total += node.val
            node.val = total
            node = node.left
        return root


class Solution(object):
    def convertBST(self, root):
        import pdb; pdb.set_trace()
        if not root:
            return root
        node = root
        total = 0
        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                successor = node.right
                while successor.left != node and successor.left:
                    successor = successor.left
                if not successor.left:
                    successor.left = node
                    node = node.right
                else:
                    successor.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root




def preorder(node):
    if not node:
        return
    preorder(node.left)
    print(node.val, end=" ")
    preorder(node.right)

def find_pre(node):
    node = node.left
    while node.right:
        node = node.right
    return node


def morris_inorder(root):
    node = root
    while node:
        if not node.left:
            print(node.val, end=" ")
            node = node.right
        else:
            predecessor = node.left
            while predecessor.right != node and predecessor.right:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                print(node.val, end=" ")
                node = node.right


t = TreeNode(4)
t.left = TreeNode(1)
t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
t.left.right.right = TreeNode(3)
t.right = TreeNode(6)
t.right.left = TreeNode(5)
t.right.right = TreeNode(7)
t.right.right.right = TreeNode(8)
preorder(t)
print("\n")
morris_inorder(t)
print("\n")

Solution().convertBST(t)
preorder(t)
