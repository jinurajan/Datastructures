"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if not root:
    return result
  q = [root]
  level = 0
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
    if level % 2 == 1:
      result.append(level_nodes[::-1])
    else:
      result.append(level_nodes)
    level+= 1
  return result



  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
