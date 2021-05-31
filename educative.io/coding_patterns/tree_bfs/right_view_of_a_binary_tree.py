"""
Right View of a Binary Tree (easy) #
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  if not root:
    return result
  q = [root]
  while q:
    l = len(q)
    level_nodes = []
    for i in range(l):
      node = q.pop(0)
      level_nodes.append(node)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.append(level_nodes[-1])

  return result


def tree_right_view(root):
  result = []
  if not root:
    return result
  q = [root]
  while q:
    l = len(q)
    for i in range(l):
      node = q.pop(0)
      if i == l-1:
          result.append(node)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.append(level_nodes[-1])

  return result



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()







