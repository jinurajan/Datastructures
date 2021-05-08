"""
Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20

"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        res[0][0] = 1
        direction = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        move = (0, 1)
        value = 2
        row = 0
        col = 0
        step = 1
        while step < n ** 2:
            if 0 <= row + move[0] < n and 0 <= col + move[1] < n and res[row + move[0]][col + move[1]] == 0:
                res[row + move[0]][col + move[1]] = value
                row += move[0]
                col += move[1]
                value += 1
                step += 1
            else:
                move = direction[move]
        return res
