"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        if not rows:
            return matrix
        cols = len(matrix[0])
        is_col = False
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0
        return matrix



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_be_zeroed = set()
        cols_to_be_zeroed = set()
        rows = len(matrix)
        if not rows:
            return matrix
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_to_be_zeroed.add(i)
                    cols_to_be_zeroed.add(j)
        for row in rows_to_be_zeroed:
            for j in range(cols):
                matrix[row][j] = 0
        for col in cols_to_be_zeroed:
            for j in range(rows):
                matrix[j][col] = 0
        return matrix


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_be_zeroed = set()
        cols_to_be_zeroed = set()
        rows = len(matrix)
        if not rows:
            return matrix
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_to_be_zeroed.add(i)
                    cols_to_be_zeroed.add(j)
        for row in rows_to_be_zeroed:
            matrix[row] = [0] * cols
        for col in cols_to_be_zeroed:
            for j in range(rows):
                matrix[j][col] = 0
        return matrix

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_be_zeroed = set()
        cols_to_be_zeroed = set()
        rows = len(matrix)
        if not rows:
            return matrix
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_to_be_zeroed.add(i)
                    cols_to_be_zeroed.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in rows_to_be_zeroed or j in cols_to_be_zeroed:
                    matrix[i][j] = 0
        return matrix
        
        