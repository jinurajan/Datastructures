"""
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  if not root:
    return result
  q = [root]
  while q:
    l = len(q)
    level_sum = 0
    level_count = 0
    for i in range(l):
      node = q.pop(0)
      level_sum += node.val
      level_count += 1
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.append(level_sum/level_count)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
