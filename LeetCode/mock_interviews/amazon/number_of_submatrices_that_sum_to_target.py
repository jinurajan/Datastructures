"""
Number of Submatrices That Sum to Target

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

"""
from typing import List

from collections import defaultdict


class Solution1:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])

        # compute 2D prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

        count = 0
        # reduce 2D problem to 1D one
        # by fixing two rows r1 and r2 and
        # computing 1D prefix sum for all matrices using [r1..r2] rows
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                h = defaultdict(int)
                h[0] = 1

                for col in range(1, c + 1):
                    # current 1D prefix sum
                    curr_sum = ps[r2][col] - ps[r1 - 1][col]

                    # add subarrays which sum up to (curr_sum - target)
                    count += h[curr_sum - target]

                    # save current prefix sum
                    h[curr_sum] += 1

        return count


from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])

        # compute 2D prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

        count = 0
        # reduce 2D problem to 1D one
        # by fixing two columns c1 and c2 and
        # computing 1D prefix sum for all matrices using [c1..c2] columns
        for c1 in range(1, c + 1):
            for c2 in range(c1, c + 1):
                h = defaultdict(int)
                h[0] = 1

                for row in range(1, r + 1):
                    # current 1D prefix sum
                    curr_sum = ps[row][c2] - ps[row][c1 - 1]

                    # add subarrays which sum up to (curr_sum - target)
                    count += h[curr_sum - target]

                    # save current prefix sum
                    h[curr_sum] += 1

        return count


# matrix = [[0,1,0],[1,1,1],[0,1,0]]
# target = 0
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 9
print(Solution1().numSubmatrixSumTarget(matrix, target))