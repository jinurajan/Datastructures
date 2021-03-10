"""
Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.


Follow up: Traversing the tree to count the number of nodes in the tree is an easy solution but with O(n) complexity. Could you find a faster algorithm?

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def depth(node, depth):
            if not node:
                return depth
            depth(node.left, depth+1)

        def exists(n):
            node = root
            lo, hi = 0, N
            for i in range(d):
                mid = (lo + hi) // 2
                if n <= mid:
                    hi = mid
                    node = node.left
                else:
                    low = mid+1
                    node = node.right
            return node

        d = depth(root, 0) -1 
        # if it has all nodes required see if there is any missing
        N = pow(2, d) - 1
        low, high = 0, N
        while low <= high:
            mid = low + high // 2
            if exists(mid):
                low = mid + 1
            else:
                high = mid-1
        return N + low

