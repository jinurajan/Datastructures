# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution1:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        Q = deque([root])
        result = []
        while Q:
            level_nodes = []
            size = len(Q)
            while size:
                node = Q.popleft()
                if node and node.val:
                    level_nodes.append(node.val)
                else:
                    level_nodes.append(None)
                if node:
                    Q.append(node.left)
                if node:
                    Q.append(node.right)
                size -= 1
            result.append(level_nodes)
        result.pop(-1)
        failed_level = len(result)
        for i in range(len(result)):
            values = [x for x in result[i] if x is not None]
            if len(values) < pow(2, i):
                failed_level = i
                break
        if failed_level == len(result):
            return True
        if failed_level == len(result)-1:
            # failed at last level check more
            # find last occurence of not none and first occurence of None
            last_not_none = 0
            first_none = len(result[failed_level])
            for i in range(len(result[failed_level])):
                if result[failed_level][i] is None:
                    first_none = min(i, first_none)
                else:
                    last_not_none = max(last_not_none, i)
            return last_not_none < first_none
        return False


class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))
        return  nodes[-1][1] == len(nodes)





t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
print(Solution().isCompleteTree(t))
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.right = TreeNode(7)
print(Solution().isCompleteTree(t))
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print(Solution().isCompleteTree(t))

