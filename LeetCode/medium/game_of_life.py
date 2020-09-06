"""
Game of Life #medium
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""


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

i = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
output = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
print(Solution().gameOfLife(i))
