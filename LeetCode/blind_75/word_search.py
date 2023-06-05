"""
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        def backtrack(x, y, suffix):
            if len(suffix) == 0:
                return True
            if x < 0 or x == self.ROWS or col < 0 or y == self.COLS \
                or self.board[x][y] != suffix[0]:
                return False
            ret = False
            self.board[x][y] = "#"
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ret = backtrack(x+dx, y+dy, suffix[1:])
                if ret:
                    break
                self.board[x][y] = suffix[0]
            return ret


        for row in range(self.ROWS):
            for col in range(self.COLS):
                if backtrack(row, col, word):
                    return True
        return False
        