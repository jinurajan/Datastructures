"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  if not root:
    return 0

  count = 0

  def dfs(node, s, path):
    nonlocal count
    if not node:
      return 0
    path.append(node.val)
    path_count, path_sum = 0, 0
    for i in range(len(path)-1, -1, -1):
      path_sum += path[i]
      if path_sum == s:
        count += 1
    path_count += dfs(node.left, s, path)
    path_count += dfs(node.right, s, path)
    path.pop()
    return path_count

  dfs(root, S, [])
  return count


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
