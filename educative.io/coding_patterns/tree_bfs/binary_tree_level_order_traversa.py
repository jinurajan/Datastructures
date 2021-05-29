"""
level order in the reverse order
"""

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  if not root:
    return result
  q = [root]
  while q:
    l = len(q)
    level_nodes = []
    for i in range(l):
      node = q.pop(0)
      level_nodes.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.appendleft(level_nodes)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
