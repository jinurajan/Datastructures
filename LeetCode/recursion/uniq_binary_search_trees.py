"""
96. Unique Binary Search Trees (Medium)

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19


T[N] = T[0]*T[N-1]+T[1]*T[N-2]+ T[2]* T[N-2] and so on

G(3) = F(1, 3) + F(2, 2)+ F(3, 3)
"""
class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        result = [0]* (n+1)
        result[0] = 1
        result[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                result[i] += result[j]* result[i-j-1]
        return result[n]


class Solution(object):
    mem = {(0, 1): 1}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count_bsts(1, n)

    def count_bsts(self, min_val, max_val):
        if min_val >= max_val:
            return 1
        elif (min_val, max_val) in self.mem:
            return self.mem[(min_val, max_val)]
        elif (max_val, min_val) in self.mem:
            return self.mem[(max_val, min_val)]
        bsts_count = 0
        for i in range(min_val, max_val+1):
            left_count = self.count_bsts(min_val, i-1)
            right_count = self.count_bsts(i+1, max_val)
            bsts_count += left_count * right_count
        self.mem[(min_val, max_val)] = bsts_count
        return bsts_count







print Solution().numTrees(0)
print Solution().numTrees(1)
print Solution().numTrees(2)
print Solution().numTrees(3)
print Solution().numTrees(4)
print Solution().numTrees(5)





