"""
Given a chessboard of size n×n, determine how many ways n queens can be placed on the board, such that no two queens attack each other.

A queen can move horizontally, vertically, and diagonally on a chessboard. One queen can be attacked by another queen if both share the same row, column, or diagonal.

1 <= n <= 9
"""

def solve_n_queens(n):
  # Write your code here
  cols = [0] * n
  l_diag = [0] * (2*n+1)
  anti_diag = [0] * (2*n+1)
  ways = 0
  def search(y):
    nonlocal ways
    if y == n:
      ways += 1
      return
    for x in range(n):
      if cols[x] or l_diag[x+y] or anti_diag[x-y+n-1]:
        continue
      cols[x] = l_diag[x+y] = anti_diag[x-y+n-1] = 1
      search(y+1)
      cols[x] = l_diag[x+y] = anti_diag[x-y+n-1] = 0
  search(0)
  return ways
  

def main():
    n = [4]
    for i in range(len(n)):
        print(i+1, ". Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = solve_n_queens(n[i])
        print("-"*100, "\n", sep="")
        print(f"Number of ways queen can be placed is {res}")


if __name__ == '__main__':
    main()