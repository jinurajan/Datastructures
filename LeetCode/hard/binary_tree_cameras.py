"""
Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


class Solution(object):
    def minCameraCover(self, root):
        self.count = 0
        covered = {None}

        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (parent is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.count += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root, None)
        return self.count