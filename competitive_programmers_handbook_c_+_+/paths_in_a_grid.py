"""

"""

def max_sum_in_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for j in range(cols+1)] for i in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]
        print(dp)
    return dp[-1][-1]



grid = [
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8]
]
print(max_sum_in_grid(grid))