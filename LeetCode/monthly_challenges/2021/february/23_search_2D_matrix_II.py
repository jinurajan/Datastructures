"""
Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        # single row
        rows = len(matrix)
        columns = len(matrix[0])
        def binary_search_2d(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            elif target > matrix[bottom][right] or target < matrix[top][left]:
                return False
            r_mid = (top + bottom) // 2
            c_mid = (left + right) // 2
            if matrix[r_mid][c_mid] == target:
                return True
            elif matrix[r_mid][c_mid] > target:
                return binary_search_2d(left, c_mid, top, r_mid) or binary_search_2d(
                    c_mid+1, right, top, r_mid) or binary_search_2d(
                    left, c_mid, r_mid+1, bottom)
            else:
                return binary_search_2d(left, c_mid, r_mid+1, bottom) or binary_search_2d(
                    c_mid+1, right, top, r_mid) or binary_search_2d(
                    c_mid+1, right, r_mid+1, bottom
                )
        return binary_search_2d(0, columns-1, 0, rows-1)



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        col = columns-1
        while row >= 0 and row < rows and col >= 0 and col < columns:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(Solution().searchMatrix(matrix, target))
print(Solution().searchMatrix(matrix, 1000))