"""
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not List:
            # list is []
            return False
        rows = len(matrix)
        if not rows:
            return False
        columns = len(matrix[0])
        if not rows or not columns:
            return False
        rows -= 1
        columns -= 1
        if not rows and not columns:
            return True if matrix[rows][columns] == target else False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        def binary_search(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            elif target > matrix[bottom][right] or target < matrix[top][left]:
                return False
            
            rmid = top + (bottom - top) // 2
            cmid = left + (right - left) // 2
            
            if matrix[rmid][cmid] == target:
                return True
            elif matrix[rmid][cmid] > target:
                return binary_search(left, cmid, top, rmid) or binary_search(cmid+1, right, top, rmid) or binary_search(left, cmid, rmid+1, bottom)
            else:
                return binary_search(left, cmid, rmid+1, bottom) or binary_search(cmid+1, right, top, rmid) or binary_search(cmid+1, right, rmid+1, bottom)

        return binary_search(0, columns, 0, rows)



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        
        
        while l<=r:
            mid=(l+r)//2
            nums=matrix[mid//n][mid%n]
            if nums==target:
                return True
            elif nums<target:
                l=mid+1
            else:
                r=mid-1
        return False
            


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(Solution().searchMatrix(
  matrix, 3))
print(Solution().searchMatrix(
    matrix, 1))
print(Solution().searchMatrix(
  matrix, 50))
print(Solution().searchMatrix(
  matrix, 11))
print(Solution().searchMatrix(
  matrix, 20))
print(Solution().searchMatrix(
    matrix, 10))
print(Solution().searchMatrix(
    matrix, 33))
print(Solution().searchMatrix(
    matrix, 0))
print(Solution().searchMatrix(
    matrix, 51))

print(Solution().searchMatrix(
    [[1]], 1))
print(Solution().searchMatrix(
    [], 0))
print(Solution().searchMatrix(
    [[]], 0))



