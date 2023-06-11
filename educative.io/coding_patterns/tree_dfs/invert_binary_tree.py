"""
Given the root node of a binary tree, convert the binary tree into its mirror image.
"""


def mirror_binary_tree(root):
  
  if not root:
    return None
  
  right = mirror_binary_tree(root.right)
  left = mirror_binary_tree(root.left)
  root.left , root.right = right, left
  return root


def mirror_binary_tree(root):
  
  if not root:
    return None
  
  q = [root]
  while q:
    node = q.pop(0)
    node.left, node.right = node.right, node.left
    if node.left:
      q.append(node.left)
    if node.right:
      q.append(node.right)
    
  return root