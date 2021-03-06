


class Node(object):
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class BST(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self.insert(self.root, data)
        return self.root

    def insert(self, node, data):
        if node is None:
            return Node(data)
        if node.data > data:
            # belongs in the left
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def min_value_node(self, node):
        current = node
        while current is not None:
            current = current.left

        return current

    def delete(self, data):
        self.remove(self.root, data)

    def remove(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return None
        if node.data > data:
            node.left = self.remove(node.left, data)
        elif node.data < data:
            node.right = self.remove(node.right, data)
        else:
            if node.left is None:
                # one child or no child
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        return node

    def inorder_traversal(self, node):
        # LRoR
        if node is None:
            return
        else:
            self.inorder_traversal(node.left)
            print node.data,
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is None:
            return
        else:
            print node.data,
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is None:
            return
        else:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print node.data,

    def height(self, node):
        if node is None:
            return 0
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


if __name__ == "__main__":
    bst = BST()
    bst.add(4)
    bst.add(3)
    bst.add(6)
    bst.add(7)
    bst.add(1)
    bst.add(2)
    bst.add(5)
    bst.inorder_traversal(bst.root)
    print "\n"
    bst.preorder_traversal(bst.root)
    print "\n"
    bst.postorder_traversal(bst.root)
    print "\n"
    print bst.height(bst.root)
    bst.delete(4)
    print bst.inorder_traversal(bst.root)
