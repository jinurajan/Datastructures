"""
Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        if not rows or not cols:
            return board
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        def no_of_live_neighbors(x, y):
            count = 0
            for dx, dy in neighbors:
                if 0 <= x + dx <= rows - 1 and 0 <= y + dy <= cols - 1:
                    if abs(board[x + dx][y + dy]) == 1:
                        count += 1
            return count

        for i in range(rows):
            for j in range(cols):
                live_neighbours = no_of_live_neighbors(i, j)
                if board[i][j] == 0 and live_neighbours == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[i][j] = -1
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        states = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                states[(i, j)] = self.count_live(board, i, j)
        print states
        for pos in states:
            i, j = pos
            live_count = states[pos]
            if board[i][j] == 1:
                if live_count < 2 or live_count > 3:
                        board[i][j] = 0
            elif live_count == 3:
                board[i][j] = 1
        return board

    @staticmethod
    def count_live(board, i, j):
        neighbors = [(i, j-1), (i, j+1), (i-1, j), (i+1, j),
                     (i-1, j+1), (i+1, j-1), (i-1, j-1), (i+1, j+1)]
        count = 0
        for pair in neighbors:
            if pair[0] < 0 or pair[1] < 0 or pair[0] >= len(board) or pair[1] >= len(board[i]):
                continue
            else:
                count += board[pair[0]][pair[1]]
        return count