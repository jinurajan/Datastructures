"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        edge cases
        matrix is of size 1 and target is not the value
        matrix has only one row / one column
        """
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        if not rows or not cols:
            return False
        rows -= 1
        cols -= 1
        if not rows and not cols:
            return True if matrix[rows][cols] == target else False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        def binary_search(left, right, top, bottom):
            if left > right or top > bottom :
                return False
            elif target > matrix[bottom][right] or target < matrix[top][left]:
                return False
            
            rmid = (top + bottom )// 2
            cmid = (left+right) // 2

            if matrix[rmid][cmid] == target:
                return True
            elif matrix[rmid][cmid] > target:
                return binary_search(left, cmid, top, rmid) or binary_search(cmid+1, right, top, rmid) or binary_search(left, cmid, rmid+1, bottom)
            else:
                return binary_search(left, cmid, rmid+1, bottom) or binary_search(cmid+1, right, top, rmid) or binary_search(cmid+1, right, rmid+1, bottom)

        return binary_search(0, cols, 0, rows)