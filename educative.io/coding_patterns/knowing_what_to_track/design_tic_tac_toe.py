"""
Suppose that two players are playing a tic-tac-toe game on an n *n board. They are following specific rules to play and win the game:

A move is guaranteed to be valid if a mark is placed on an empty block.
No more moves are allowed once a winning condition is reached.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

"""

class TicTacToe:
    
    # Constructor will be used to initialize TicTacToe data members 
    def __init__(self, n): 
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
               

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def move(self, row, col, player):
        # 1 for player 1 -1 for player 2
        current_player = -1
        if player == 1:
            current_player = 1
        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player
        
        if row + col == self.n-1:
            self.anti_diagonal += current_player

        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        return 0



# Driver code
def main():
    n = 3
    inputs = [  [[0, 1, 1], [1, 0, 2], [2, 1, 1], [1, 2, 2], [0, 2, 1], [2, 2, 2], [1, 1, 1]], 
                [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [1, 0, 1], [2, 0, 2], [1, 2, 1]] ]
    
    for game in range(2):
        fill_grid = []
        print("Game ",(game+1), ": \n", sep="")
        tic_tac_toe_obj = TicTacToe(n)
        win = 0
        for i in range(0, len(inputs[game])):
            print("Move ", (i+1), ":\tPlayer ", inputs[game][i][2], " places their mark at ", inputs[game][i][0], ", ", inputs[game][i][1] , sep="", end="")

            win = tic_tac_toe_obj.move(inputs[game][i][0], inputs[game][i][1], inputs[game][i][2])

            if (win == 0):
                print("\tNo one wins the game")
                print("-" * 100)
            else:
                print("\tPlayer", win, "wins the game")
                print("-" * 100)
                break


if __name__ == '__main__':
    main() 