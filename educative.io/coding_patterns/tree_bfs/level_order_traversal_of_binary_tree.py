"""

"""

# Import required functions
from collections import deque

# Template for binary tree node

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0

class BinaryTree:
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # for BST insertion
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if not self.root:
            self.root = new_node
        else:
            parent = None
            temp_pointer = self.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

# Tip: You may use some of the code templates provided
# in the support files

def level_order_traversal(root):
    result = ""
    # Write your code here
    if not root:
        return "None"
    queue = [root]
    while queue:
        l = len(queue)
        for i in range(l):
            node = queue.pop(0)
            result += str(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i < l-1:
                result += ", "
            else:
                if not queue:
                    continue
                result += " : "
    return result



def main():
    # Creating a binary tree
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)

    # Creating a right degenerate binary tree
    input2 = sorted(input1)
    tree2 = BinaryTree(input2)

    # Creating a left degenerate binary tree
    input2.reverse()
    tree3 = BinaryTree(input2)

    # Creating a single node binary tree
    tree4 = BinaryTree(100)

    roots = [tree1.root, tree2.root, tree3.root, tree4.root, None]

    for i in range(len(roots)):
        print(i+1, ".\tBinary Tree:", sep = "")
        display_tree(roots[i])
        # Printing the in-order list using the method we just implemented
        print("\n\tLevel order traversal: ", sep = "", end = "")
        print(level_order_traversal(roots[i]))
        print("\n", "-"*100, "\n", sep = "")


if __name__ == '__main__':
    main()
