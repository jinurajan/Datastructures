"""
Unique Binary Search Trees II (Hard)

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def construct_trees(start, end):
            array = []
            if start > end:
                array.append(None)
                return array
            for i in range(start, end+1):
                left_tree = construct_trees(start, i-1)
                right_tree = construct_trees(i+1, end)
                for j in range(len(left_tree)):
                    left = left_tree[j]
                    for k in range(len(right_tree)):
                        right = right_tree[k]
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        array.append(node)
            return array

        return construct_trees(1, n)


def preorder(root):
    if root is None:
        return
    print(root.val),
    preorder(root.right)
    preorder(root.left)


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        hash_set = {}
        def construct_trees(start, end):
            if start > end:
                return [None]
            if (start, end) in hash_set:
                return hash_set[(start, end)]
            result = []
            for i in range(start, end + 1):
                left_tree = construct_trees(start, i-1)
                right_tree = construct_trees(i+1, end)
                for j in range(len(left_tree)):
                    left = left_tree[j]
                    for k in range(len(right_tree)):
                        right = right_tree[k]
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        result.append(node)
            hash_set[(start, end)] = result
            return result

        return construct_trees(1, n)





for i in range(6):
    l = Solution().generateTrees(i)
    for root in l:
        preorder(root)
        print "\n"
    print "***************"


