"""
	Binary Search Tree
"""


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, node, data):
		if node is None:
			return Node(data)
		if data > node.data:
			node.right = self.insert(node.right, data)
		else:
			node.left = self.insert(node.left, data)
		return node


	def inorder_traversal(self, node):
		if node is not None:
			self.inorder_traversal(node.left)
			print node.data,
			self.inorder_traversal(node.right)


if __name__ == "__main__":
	bst = BST()
	bst.root = bst.insert(None, 3)
	bst.insert(bst.root, 4)
	bst.insert(bst.root, 1)
	bst.inorder_traversal(bst.root)
