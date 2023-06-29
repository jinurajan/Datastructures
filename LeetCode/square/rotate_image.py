"""
Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n % 2):
            for j in range(n//2):
                # print(i, j)
                print(n-1-j, i)
                print(n-1-i, n-j-1)
                print(j, n-1-i)
                print(i, j)
                tmp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp
                print("******")


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Solution().rotate(matrix=matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix=matrix)
print(matrix)