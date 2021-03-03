"""
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('null')
        while res and res[-1] == 'null':
            res.pop()
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == '[]':
            return None
        nodes = data.split(",")
        if not nodes:
            return None
        root = TreeNode(int(nodes.pop(0)))
        if not nodes:
            return root
        q = deque([root])
        while q and nodes:
            size = len(q)
            while size:
                node = q.popleft()
                l = nodes.pop(0) if nodes else None
                r = nodes.pop(0) if nodes else None
                if l and l != 'null':
                    node.left = TreeNode(int(l))
                    q.append(node.left)
                if r and r != 'null':
                    node.right = TreeNode(int(r))
                    q.append(node.right)
                size -= 1
        return root

    def inorder(self, node):
        if not node:
            return
        print(node.val)
        self.inorder(node.left)
        self.inorder(node.right)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node, string):
            if not node:
                string += 'None,'
            else:
                string += f"{node.val},"
                string = dfs(node.left, string)
                string = dfs(node.right, string)
            return string

        return dfs(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(nodes):
            if nodes[0] == 'None':
                nodes.pop(0)
                return None

            root = TreeNode(nodes[0])
            nodes.pop(0)
            root.left = dfs(nodes)
            root.right = dfs(nodes)
            return root

        nodes = data.split(',')
        return dfs(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))