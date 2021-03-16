"""
Construct Binary Tree from String
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.
0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
class Solution:
 def str2tree(self, s: str) -> TreeNode:
     if not s:
         return None
     start = 0
     def str2treehelper(s):
         nonlocal start
         if start >= len(s):
             return
         neg = False
         if s[start] =='-':
             neg = True
             start += 1
         num = 0
         while start < len(s) and s[start].isdigit():
             digit = int(s[start])
             num = num*10+ digit
             start += 1
         if neg:
             num = -num
         root = TreeNode(num)
         if start >= len(s):
             return root
         if start < len(s) and s[start] == '(':
             start += 1
             root.left = str2treehelper(s)
         if start < len(s) and s[start] == ')':
             start += 1
             return root
         if start < len(s) and s[start] == '(':
             start += 1
             root.right = str2treehelper(s)
         if start < len(s) and s[start] == ')':
             start += 1
             return root
         return root
     return str2treehelper(s)


def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val, end= " ")
    inorder_traversal(node.right)


s = "4(2(3)(1))(6(5))"
root = Solution().str2tree(s)
inorder_traversal(root)

s = "4(2(3)(1))(6(5)(7))"
s = "-4(2(3)(1))(6(5)(7))"