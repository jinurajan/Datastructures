"""
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""

from typing import List



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        l_diag = [0] * (2 * n + 1)
        anti_diag = [0] * (2 * n + 1)
        result = []

        def format_queens(positions):
            res = [['.' for i in range(n)] for j in range(n)]
            for x, y in positions:
                res[x][y] = 'Q'
            return ["".join(r) for r in res]

        def search(y):
            if y == n:
                result.append(format_queens(positions[:]))
                return
            for x in range(n):
                if cols[x] or l_diag[x + y] or anti_diag[x - y + n - 1]:
                    continue
                cols[x] = l_diag[x + y] = anti_diag[x - y + n - 1] = 1
                positions.append((x, y))
                search(y + 1)
                cols[x] = l_diag[x + y] = anti_diag[x - y + n - 1] = 0
                positions.pop()

        positions = []
        search(0)
        return result
