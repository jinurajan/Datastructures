"""
Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
"""
class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        for line in range(1, n+1):
        	C = 1
        	for i in range(1, line+1):
        		print C,
        		C = int(C * (line-i)/i)
        	print ""


print Solution().generate(5)