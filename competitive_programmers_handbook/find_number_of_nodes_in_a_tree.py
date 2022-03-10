"""
Use Dynamic Programming to find the number of elements in the subtree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

def find_no_of_nodes_of_each_subtree(root):
    count = defaultdict(int)

    def dfs(node, prev_node):
        count[node] = 1
        # this can change if the tree is not binary: 
        # in that adjascency list can be used
        adj = []
        if node.left:
            adj.append(node.left)
        if node.right:
            adj.append(node.right)
        for neighbour in adj:
            if node == prev_node:
                continue
            dfs(neighbour, node)
            count[node] += count[neighbour]
    dfs(root, None)
    return count

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
tree.right.right.right = TreeNode(8)

print(find_no_of_nodes_of_each_subtree(tree))

