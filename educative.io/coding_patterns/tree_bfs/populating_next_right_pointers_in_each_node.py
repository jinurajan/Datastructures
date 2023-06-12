"""
Given a binary tree, connect all nodes of the same hierarchical level. We need to connect them from left to right, so that the next pointer of each node points to the node on its immediate right. The next pointer of the right-most node at each level will be NULL.

For this problem, each node in the binary tree has one additional pointer (the next pointer) along with the left and right pointers.


"""

from binary_tree import *
from binary_tree_node import *


def connect_next_level(head):
    current = head
    next_level_head = None
    prev = None
    while current:
        if current.left and current.right:
            if not next_level_head:
                next_level_head = current.left
            current.left.next = current.right

            if prev:
                prev.next = current.left
            
            prev = current.right
        elif current.left:
            if not next_level_head:
                next_level_head= current.left
            
            if prev:
                prev.next = current.left
            prev = current.left
        
        elif current.right:
            if not next_level_head:
                next_level_head= current.right
            
            if prev:
                prev.next = current.right
            prev = current.right
        
        current = current.next
    
    if prev:
        prev.next = None
    
    return next_level_head

# Function to populate same level pointers
def populate_next_pointers(node):
    if node:
        node.next = None
        while True:
            node = connect_next_level(node)
            if not node:
                break

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
