"""
Pascal's Triangle II
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        C = 1
        rowIndex = rowIndex + 1
        for i in range(1, rowIndex + 1):
            result.append(C)
            C = int(C * (rowIndex - i)/i)

        return result


# print Solution().getRow(1)
# print Solution().getRow(2)
print Solution().getRow(3)
# print Solution().getRow(4)
# print Solution().getRow(5)
# print Solution().getRow(6)
