"""
Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):

#     # def pathSum(self, root, sum_val):
#     #     """
#     #     :type root: TreeNode
#     #     :type sum: int
#     #     :rtype: int
#     #     """
#     #     if root is None:
#     #         return 0
#     #     if root.val == sum_val or sum_val == 0:
#     #         return 1
#     #     diff = sum_val - root.val if root.val <= sum_val else sum_val
#     #     l = self.pathSum(root.left, diff)
#     #     r = self.pathSum(root.right, diff)
#     #     return l + r

#     def pathSum(self, root, sum_val):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: int
#         """
#         self.result, self.count = 0, defaultdict(int)
#         self.count[sum_val] = 1
#         self.dfs(root, sum_val, 0)
#         return self.result

#     def dfs(self, root, sum_val, root_sum):
#         if root is None:
#             return 0
#         root_sum += root.val
#         self.result += self.count[root_sum]
#         self.count[root_sum] += 1
#         self.dfs(root.left, sum_val, root_sum)
#         self.dfs(root.right, sum_val, root_sum)

    # def FindpathSum(self, root, sum_val):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     path = []
    #     self.find_paths_sum(root, 0, sum_val, path)

    # def find_paths_sum(self, root, curr_sum, sum_val, path):
    #     if root is None:
    #         return
    #     curr_sum += root.val
    #     path.append(root.val)
    #     if curr_sum == sum_val:
    #         print "path found:", path
    #         for i in range(len(path)):
    #             print path[i],
    #         print ""
    #     if root.left is not None:
    #         self.find_paths_sum(root.left, curr_sum, sum_val, path)
    #     if root.right is not None:
    #         self.find_paths_sum(root.right, curr_sum, sum_val, path)

    #     path.pop(-1)

    # def pathSum(self, root, sum_val):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     self.count = defaultdict(int)
    #     self.find_all_paths_sum(root, sum_val, 0)
    #     print self.count[sum_val]

    # def find_all_paths_sum(self, root, sum_val, sum_so_far):
    #     if root is None:
    #         return
    #     sum_so_far += root.val
    #     self.count[sum_so_far] += 1
    #     if sum_so_far > sum_val:
    #         sum_so_far = 0
    #     self.find_all_paths_sum(root.left, sum_val, sum_so_far)
    #     self.find_all_paths_sum(root.right, sum_val, sum_so_far)


class Solution(object):
    def dfs(self, root, sum, root_sum):
        if not root:
            return None
        print root.val, root_sum, self.count
        root_sum += root.val
        self.result += self.count[root_sum]
        print root_sum + sum
        self.count[root_sum + sum] += 1
        self.dfs(root.left, sum, root_sum)
        self.dfs(root.right, sum, root_sum)
        self.count[root_sum + sum] -= 1

    def pathSum(self, root, sum):
        self.result, self.count = 0, defaultdict(int)
        self.count[sum] = 1
        self.dfs(root, sum, 0)
        return self.result


def inorder_traversal(root):
    if root is None or root.val is 0:
        return
    inorder_traversal(root.left)
    print root.val,
    inorder_traversal(root.right)

if __name__ == "__main__":
    # root = TreeNode(10)
    # root.left = TreeNode(5)
    # root.right = TreeNode(-3)
    # root.right.right = TreeNode(11)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(2)
    # root.left.right.right = TreeNode(1)
    # root.left.left.left = TreeNode(3)
    # root.left.left.right = TreeNode(-2)
    # sum_val = 8
    # print Solution().pathSum(root, sum_val) == 3

    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    # root.left.left = TreeNode(11)
    # root.left.right = None
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)
    # # print inorder_traversal(root)
    # sum_val = 22
    # print Solution().pathSum(root, sum_val) == 3

    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    sum_val = -1
    print Solution().pathSum(root, sum_val) == 1
