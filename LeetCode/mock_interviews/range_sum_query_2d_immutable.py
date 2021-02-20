"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

"""

from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sum += self.matrix[i][j]
        return sum


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not len(matrix) or not len(matrix[0]):
            return
        self.matrix = matrix
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        self.dp = [[0 for j in range(columns+1)] for i in range(rows)]
        for r in range(rows):
            for c in range(columns):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.dp)
        sum = 0
        for i in range(row1, row2+1):
            sum += self.dp[i][col2+1] - self.dp[i][col1]
        return sum



matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

(row1, col1) = (2, 1)
(row2, col2) = (4, 3)
print(NumMatrix(matrix).sumRegion(row1, col1, row2, col2))
# print(NumMatrix([]))
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
