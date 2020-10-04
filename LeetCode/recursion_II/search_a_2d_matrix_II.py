"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution2:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bs_row(matrix, col_no, l, r, target):
            if l <= r:
                mid = (l + r) // 2
                if matrix[mid][col_no] == target:
                    return True
                if matrix[mid][col_no] > target:
                    return bs_row(matrix, col_no, l, mid-1, target)
                return bs_row(matrix, col_no, mid+1, r, target)
            return l

        def bs_column(matrix, row_no, l, r, target):
            if l <= r:
                mid = (l + r) // 2
                if matrix[row_no][mid] == target:
                    return True
                if matrix[row_no][mid] > target:
                    return bs_column(matrix, row_no, l, mid-1, target)
                return bs_column(matrix, row_no, mid+1, r, target)
            return l
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False
        if m == 1:
            return bs_column(matrix, 0, 0, n-1, target) is True
        if n == 1:
            return bs_row(matrix, 0, 0, m-1, target) is True
        max_row, max_col = m-1, n-1
        min_row = 0
        min_col = 0
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while min_col <= max_col and min_row <= max_row:
            max_row = bs_column(matrix, min_col, min_row, max_row, target)
            if max_row is True:
                return True
            max_row = min(max_row, m-1)
            min_col = bs_row(matrix, max_row, min_col, max_col, target)
            if min_col is True:
                return True
            min_col += 1
            min_col = min(min_col, n-1)
        return False


class Solution1:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1

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
        
        return binary_search(left, right, top, bottom)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = cols -1
        while i < rows and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(Solution().searchMatrix(matrix, 1) == Solution1().searchMatrix(matrix, 1))
print(Solution().searchMatrix(matrix, 2) == Solution1().searchMatrix(matrix, 2))
print(Solution().searchMatrix(matrix, 3) == Solution1().searchMatrix(matrix, 3))
print(Solution().searchMatrix(matrix, 10) == Solution1().searchMatrix(matrix, 10))
print(Solution().searchMatrix(matrix, 18) == Solution1().searchMatrix(matrix, 18))


print(Solution().searchMatrix(matrix, 4) == Solution1().searchMatrix(matrix, 4))
print(Solution().searchMatrix(matrix, 5) == Solution1().searchMatrix(matrix, 5))
print(Solution().searchMatrix(matrix, 6) == Solution1().searchMatrix(matrix, 6))
print(Solution().searchMatrix(matrix, 13) == Solution1().searchMatrix(matrix, 13))
print(Solution().searchMatrix(matrix, 21) == Solution1().searchMatrix(matrix, 21))

print(Solution().searchMatrix(matrix, 7) == Solution1().searchMatrix(matrix, 7))
print(Solution().searchMatrix(matrix, 8) == Solution1().searchMatrix(matrix, 8))
print(Solution().searchMatrix(matrix, 9) == Solution1().searchMatrix(matrix, 9))
print(Solution().searchMatrix(matrix, 14) == Solution1().searchMatrix(matrix, 14))
print(Solution().searchMatrix(matrix, 23) == Solution1().searchMatrix(matrix, 23))

print(Solution().searchMatrix(matrix, 11) == Solution1().searchMatrix(matrix, 11))
print(Solution().searchMatrix(matrix, 12) == Solution1().searchMatrix(matrix, 12))
print(Solution().searchMatrix(matrix, 16) == Solution1().searchMatrix(matrix, 16))
print(Solution().searchMatrix(matrix, 17) == Solution1().searchMatrix(matrix, 17))
print(Solution().searchMatrix(matrix, 26) == Solution1().searchMatrix(matrix, 26))


print(Solution().searchMatrix(matrix, 15) == Solution1().searchMatrix(matrix, 15))
print(Solution().searchMatrix(matrix, 19) == Solution1().searchMatrix(matrix, 19))
print(Solution().searchMatrix(matrix, 22) == Solution1().searchMatrix(matrix, 22))
print(Solution().searchMatrix(matrix, 24) == Solution1().searchMatrix(matrix, 24))
print(Solution().searchMatrix(matrix, 30) == Solution1().searchMatrix(matrix, 30))

print(Solution().searchMatrix(matrix, 31) == Solution1().searchMatrix(matrix, 31))
print(Solution().searchMatrix(matrix, 0) == Solution1().searchMatrix(matrix, 0))

print(Solution().searchMatrix([], 0) == Solution1().searchMatrix([], 0))
print(Solution().searchMatrix([[]], 1) == Solution1().searchMatrix([[]], 1))
print(Solution().searchMatrix([[1], [2], [3]], 3) == Solution1().searchMatrix([[1], [2], [3]], 3))
print(Solution().searchMatrix([[1], [2], [3]], 4) == Solution1().searchMatrix([[1], [2], [3]], 4))

print(Solution().searchMatrix([[1, 4], [2, 5]], 2) == Solution1().searchMatrix([[1, 4], [2, 5]], 2))

