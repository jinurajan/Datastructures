"""
Serialize and Deserialize BST
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec1:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def preorder(node, res):
            if not node:
                res.append("X")
                return 
            res.append(str(node.val))
            preorder(node.left, res)
            preorder(node.right, res)

        res = []
        preorder(root, res)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(",")
        self.index = 0
        def dfs():
            if self.index == len(nodes) or nodes[self.index] == 'X':
                self.index += 1
                return None
            root = TreeNode(int(nodes[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

import collections

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # pre-order traverse
        if root == None:
            return ""    
        return "X".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        s = collections.deque(data.split("X"))
        
        def helper(datalist:collections.deque()) -> TreeNode:
            val = datalist.popleft()
            if val == "":
                return None
            root = TreeNode(int(val))
            root.left = helper(datalist)
            root.right = helper(datalist)
            return root
        
        return helper(s)


class Codec2:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))



def inorder(node):
    if not node:
        print("")
        return
    inorder(node.left)
    print(node.val, end= "")
    inorder(node.right)     

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(1)


ser = Codec()
deser = Codec()
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
inorder(ans)


ser = Codec1()
deser = Codec1()
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
inorder(ans)


ser = Codec2()
deser = Codec2()
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
inorder(ans)
