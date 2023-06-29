"""
Range Sum Query 2D - Mutable


Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0]* (cols+1) for _ in range(rows+1)]
        self.matrix = matrix
        for row in range(rows):
            psum = 0
            for col in range(cols):
                psum += matrix[row][col]
                self.prefix[row+1][col+1] = psum + self.prefix[row][col+1]
        

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        for r in range(row+1, len(self.prefix)):
            for c in range(col+1, len(self.prefix[0])):
                if c >= col+1:
                    self.prefix[r][c] += diff
        self.matrix[row][col] = val
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2,col2 = row1+1, col1+1, row2+1,col2+1
        upper_left = self.prefix[row1-1][col1-1]
        bottom_right = self.prefix[row2][col2]
        upper_right = self.prefix[row1-1][col2]
        bottom_left = self.prefix[row2][col1-1]

        return bottom_right - upper_right - bottom_left + upper_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)