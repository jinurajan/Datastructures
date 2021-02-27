"""
Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.


Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """ using bfs and hash map of parent nodes"""
        if not root or (not root.left and not root.right):
            return root
        parent_map = {root: None}
        Q = [root]

        while Q:
            last_level_nodes = Q[:]
            size = len(Q)
            while size:
                node = Q.pop(0)
                if node.left:
                    parent_map[node.left] = node
                    Q.append(node.left)
                if node.right:
                    parent_map[node.right] = node
                    Q.append(node.right)
                size -= 1
        if len(last_level_nodes) == 1:
            return last_level_nodes.pop()
        else:
            parent_set = set([parent_map[node] for node in last_level_nodes])
            while len(parent_set) > 1:
                parent_set = set([parent_map[node] for node in parent_set])
        return list(parent_set)[0]


class Solution1:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """using dfs and parent_map"""
        depth = {None: -1}
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        max_depth = max(depth.values())
        def find_deepest(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            L , R = find_deepest(node.left), find_deepest(node.right)
            return node if L and R else L or R
        return find_deepest(root)

from collections import namedtuple
class Solution2:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        result = namedtuple('result', ('node', 'depth'))
        def dfs(node):
            if not node:
                return result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.depth < R.depth:
                return result(R.node, R.depth+1)
            if L.depth > R.depth:
                return result(L.node, L.depth + 1)
            return  result(node, L.depth + 1)
        return dfs(root).node

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


print(Solution().subtreeWithAllDeepest(root))

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.right = TreeNode(2)

print(Solution().subtreeWithAllDeepest(root).val)
