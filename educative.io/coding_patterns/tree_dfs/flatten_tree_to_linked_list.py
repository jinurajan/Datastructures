"""
Given the root of a binary tree, the task is to flatten the tree into a linked list using the same TreeNode class. The left child pointer of each node in the linked list should always be NULL, and the right child pointer should point to the next node in the linked list. The nodes in the linked list should be in the same order as that of the preorder traversal of the given binary tree.

"""
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

def flatten_tree(root):
    if not root:
        return
    node = root
    while node:
        if node.left:
            last = node.left
            while last.right:
                last = last.right
            last.right = node.right
            node.right = node.left
            node.left = None
        node = node.right 
    return root


# Driver code
def main():

    input_trees = [
        [3, 2, 17, 1, 4, 19, 5],
        [7, 6, 5, 4, 3, 2, 1],
        [5, 4, 6, 3, 2, 7, 8, 1, 9],
        [5, 2, 1, 6, 10, 11, 44],
        [1, 2, 5, 3, 4, 6],
        [-1, -2, -5, 1, 2, -6]
    ]
    y = 1
    for i in input_trees:
        tree = BinaryTree(i)
        print(y, ". Binary tree:", sep="")
        display_tree(tree.root, None)
        tree1 = flatten_tree(tree.root)
        print(" Flattened tree:", sep="")
        display_tree(tree1, None)
        print("-"*100)
        y += 1


if __name__ == '__main__':
    main()
