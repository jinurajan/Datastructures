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
]

"""
from typing import List

class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for line in range(1, numRows+1):
            c = 1
            row_val = []
            for i in range(1, line+1):
                row_val.append(c)
                c = int(c *(line-i)/i)
            res.append(row_val)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:    return []
        if numRows == 1:    return [[1]]
        if numRows == 2:    return [[1], [1,1]]
        else:
            res = [[1], [1,1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(i-1):
                    row.append(res[i-1][j]+ res[i-1][j+1])
                res.append(row+[1])
            return res


print(Solution().generate(0))
print(Solution().generate(1))
print(Solution().generate(2))
print(Solution().generate(3))
print(Solution().generate(4))
print(Solution().generate(5))