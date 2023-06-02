"""
Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


"""


def diameter_of_binaryTree(root):
  if not root:
    return 0
  diameter = 0
  def find_dia(node):
    nonlocal diameter
    if not node:
      return 0
    l_height = find_dia(node.left)
    r_height = find_dia(node.right)
    diameter = max(l_height+r_height, diameter)
    return max(l_height, r_height) + 1
  find_dia(root)
  return diameter