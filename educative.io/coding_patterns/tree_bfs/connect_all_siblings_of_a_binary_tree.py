"""
The task is to connect all nodes in a binary tree. Connect them from left to right so that the next pointer of each node points to the node on its immediate right. The next pointer of the right-most node at each level should point to the first node of the next level in the tree.

Each node in the given binary tree for this problem includes a next pointer, along with the left and right pointers. Your solution must set the next pointer to connect the same level nodes to each other and across levels.

"""

from binary_tree import *
from binary_tree_node import *


# Tip: You may use some of the code templates provided
# in the support files

# Function to populate same level pointers
# Function to populate same level pointers
def populate_next_node_pointers(root):
    if not root:
        return root
    current, last = root, root
    while current:
        if current.left:
            last.next = current.left
            last = current.left
        if current.right:
            last.next = current.right
            last = current.right
        last.next = None
        current = current.next

# Do not modify the code below
# Function to find the given node and return its next node
def get_next_node(node, node_data):
    # Performing Binary Search
    while node and node_data != node.data:
        if node_data < node.data:
            node = node.left
        else:
            node = node.right

    # If node is not found return -1 else return its next node
    if not node:
        non_existing_node = BinaryTreeNode(-1)
        return non_existing_node
    else:
        return node.next
