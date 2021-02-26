"""
Vertical Order Traversal of a Binary Tree
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    HASH_SET = {}

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mn, mx = [0], [0]
        self.find_min_max(root, mn, mx, 0)
        result = []
        for i in range(mn[0], mx[0] + 1):
            r = []
            self.print_vertical_line(root, i, 0, r)
            result.append(r)
        return result

    def print_vertical_line(self, node, line_no, hd, r):
        if node is None:
            return
        if hd == line_no:
            if r and self.HASH_SET[r[-1]] == self.HASH_SET[node.val]:
                if node.val < r[-1]:
                    val = r.pop()
                    r.append(node.val)
                    r.append(val)
                else:
                    r.append(node.val)
            else:
                r.append(node.val)
        self.print_vertical_line(node.left, line_no, hd - 1, r)
        self.print_vertical_line(node.right, line_no, hd + 1, r)

    def find_min_max(self, node, mn, mx, hd):
        if node is None:
            return
        if hd < mn[0]:
            mn[0] = hd
        elif hd > mx[0]:
            mx[0] = hd
        if node.val not in self.HASH_SET:
            self.HASH_SET[node.val] = hd
        self.find_min_max(node.left, mn, mx, hd - 1)
        self.find_min_max(node.right, mn, mx, hd + 1)


from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        vertical_values = defaultdict(lambda:[])
        stack = deque([(root, 0)])
        min_val = 0
        max_val = 0
        result = []
        while stack:
            node, val = stack.popleft()
            if node:
                vertical_values[val].append(node.val)
                min_val = min(min_val, val)
                max_val = max(max_val, val)
                if node.left:
                    stack.append((node.left, val-1))
                if node.right:
                    stack.append((node.right, val+1))
        for i in range(min_val, max_val+1):
            result.append(vertical_values[i])
        return result



if __name__ == "__main__":
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(17)
    # print Solution().verticalTraversal(root) == [[9], [3, 15], [20], [17]]

    root = TreeNode(0)
    root.left = TreeNode(8)
    root.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.left.right = TreeNode(4)
    root.right.left.right.right = TreeNode(7)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.left.left = TreeNode(6)
    # print Solution().verticalTraversal(root) == [[8], [0, 3, 6], [1, 4, 5], [2, 7]]
    print Solution().verticalTraversal(root)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # print Solution().verticalTraversal(root) == [[4], [2], [1, 5, 6], [3], [7]]

    # root = TreeNode(0)
    # root.left = TreeNode(5)
    # root.left.left = TreeNode(9)
    # root.right = TreeNode(1)
    # root.right.left = TreeNode(2)
    # root.right.left.right = TreeNode(3)
    # root.right.left.right.right = TreeNode(8)
    # root.right.left.right.left = TreeNode(4)
    # root.right.left.right.left.left = TreeNode(6)
    # root.right.left.right.left.left.left = TreeNode(7)
    # print Solution().verticalTraversal(root) == [[9, 7], [5, 6], [0, 2, 4], [1, 3], [8]]
