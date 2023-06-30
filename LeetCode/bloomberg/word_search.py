"""
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])


        def backtrack(x, y, suffix):
            if not suffix:
                return True
            if x < 0 or x == rows or y <0 or  y == cols or board[x][y] != suffix[0]:
                return False
            ret = False
            board[x][y] = "#"
            for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                ret = backtrack(x+dx, y+dy, suffix[1:])
                if ret:
                    break
            board[x][y] = suffix[0]
            return ret
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, word):
                    return True
        return False
        
            
        
        