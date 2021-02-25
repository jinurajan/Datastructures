"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = float("inf")
        children = [root.left, root.right]
        for child in children:
            if child:
                min_depth = min(min_depth, self.minDepth(child))
        return min_depth + 1

class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = float("inf")

        def backtrack(node):
            nonlocal min_depth
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            children = [node.left, node.right]
            for child in children:
                if child:
                    min_depth = min(min_depth, backtrack(child))
            return min_depth+1

        backtrack(root)
        return min_depth


from collections import deque
class Solution1:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = deque([(root, 1)])
        while stack:
            node, depth = stack.popleft()
            if not node.left and not node.right:
                return depth
            children = [node.left, node.right]
            for child in children:
                if child:
                    stack.append((child, depth + 1))


from collections import deque
class Solution:
    # DFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = deque([(root, 1)])
        min_depth = float("inf")
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            children = [node.left, node.right]
            for child in children:
                if child:
                    stack.append((child, depth + 1))
        return min_depth

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(Solution().minDepth(root))