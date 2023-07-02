"""
Surrounded Regions


Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
from typing import List
from itertools import product
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
    
        def dfs(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'E'
            if col < cols-1:
                dfs(row, col+1)
            if row < rows-1:
                dfs(row+1, col)
            if col > 0:
                dfs(row, col-1)
            if row > 0:
                dfs(row-1, col)
        # get all boarder cells
        borders = list(product(range(rows), [0, cols-1])) \
                + list(product([0, rows-1], range(cols)))
        # mark escaped cells with E
        for row, col in borders:
            dfs(row, col)
        
        # flip the captured cells o -> x and e -> o
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
    
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                if board[row][col] != 'O':
                    continue
                board[row][col] = 'E'
                if col < cols-1:
                    queue.append((row, col+1))
                if row < rows-1:
                    queue.append((row+1, col))
                if col > 0:
                    queue.append((row, col-1))
                if row >0:
                    queue.append((row-1, col))

        # get all boarder cells
        borders = list(product(range(rows), [0, cols-1])) \
                + list(product([0, rows-1], range(cols)))
        # mark escaped cells with E
        for row, col in borders:
            bfs(row, col)
        
        # flip the captured cells o -> x and e -> o
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
        

            