"""
Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import defaultdict


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_map = defaultdict(lambda: [])

        def dfs(nested_list, depth):
            for nested in nested_list:
                if nested.isInteger():
                    depth_map[depth].append(nested.getInteger())
                else:
                    dfs(nested.getList(), depth + 1)

        dfs(nestedList, 0)
        if not depth_map:
            return 0
        max_depth = max(depth_map.keys()) + 1
        sum_val = 0
        for depth, val in depth_map.items():
            sum_val += sum([v for v in val]) * (max_depth - depth)
        return sum_val


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        node_q = deque()
        v_q = []
        for child in nestedList:
            node_q.append(child)

        while node_q:
            N = len(node_q)
            this_layer = 0
            for i in range(N):
                node = node_q.popleft()
                if node.isInteger():
                    this_layer += node.getInteger()
                else:
                    for child in node.getList():
                        node_q.append(child)
            v_q.append(this_layer)
            print("--", N, " child, v=", this_layer)

        res, level = 0, 1
        print(v_q)
        for i in range(len(v_q) - 1, -1, -1):
            res += v_q[i] * level
            level += 1
        return res












