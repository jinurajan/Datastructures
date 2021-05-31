"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  def dfs(node, index):
    if not node:
      return False
    if index >= len(sequence) or node.val != sequence[index]:
      return False
    if not node.left and not node.right and index == len(sequence)-1:
      return True
    return dfs(node.left, index+1) or dfs(node.right, index+1)

  return dfs(root, 0)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
