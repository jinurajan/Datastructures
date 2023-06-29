"""
Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        rows = len(board)
        cols = len(board[0])

        stack = [(i, j)]

        directions = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while stack:
            x, y = stack.pop()
            if board[x][y] == 'E':
                count = 0
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < rows and 0<=new_y<cols and board[new_x][new_y] == 'M':
                        count += 1
                if count == 0: 
                    board[x][y] = 'B'
                    for dx, dy in directions:
                        new_x, new_y = x+dx, y+dy
                        if 0 <= new_x < rows and 0<=new_y<cols:
                            stack.append((new_x, new_y))
                else:
                    board[x][y] = str(count)
        return board