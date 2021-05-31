"""
Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 0

        while i + 1 < len(matrix):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
            i += 1

        return True

class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        diagonals = {i: set() for i in range(-(cols - 1), rows, 1)}
        for i in range(rows):
            for j in range(cols):
                diagonals[i - j].add(matrix[i][j])
        return len([1 for k, v in diagonals.items() if len(v) == 1]) == rows + cols - 1

