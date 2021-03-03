"""
Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


Constraints:

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        head = Node()
        last = head
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    last.right = node
                    node.left = last
                    last = node
                    node = node.right
            else:
                last.right = node
                node.left = last
                last = node
                node = node.right
        last.right = head.right
        head.right.left = last
        return head.right


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def dfs(node):
            nonlocal
            first, last
            if node:
                dfs(node.left)
                if last:
                    node.left = last
                    last.right = node
                else:
                    first = node
                last = node
                dfs(node.right)

        first, last = None, None
        dfs(root)
        last.right = first
        first.left = last
        return first
