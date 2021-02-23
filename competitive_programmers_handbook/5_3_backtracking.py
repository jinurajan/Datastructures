"""
Backtracking
consider the problem of calculating the number of ways n queens can be placed on an n by n chessboard so that no two queens attack each other. For example, when n = 4, there are two possible solutions
"""

def find_no_of_ways(n):
    count = 0
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for x in range(n):
            if col[x] or diag1[x+row] or diag2[x-row+n-1]:
                continue
            col[x], diag1[row+x], diag2[x-row+n-1] = 1, 1, 1
            backtrack(row+1)
            col[x], diag1[row + x], diag2[x-row+n-1] = 0, 0, 0
    col = [0 for i in range(n)]
    diag1 = [0 for i in range(2*n-1)]
    diag2 = [0 for i in range(2*n-1)]
    backtrack(0)
    return count

def find_combinations_of_queens(n):
    result = []
    combination = []
    def backtrack(row):
        if row == n:
            result.append(combination[:])
            return
        for x in range(n):
            if col[x] or diag1[x+row] or diag2[x-row+n-1]:
                continue
            col[x], diag1[row+x], diag2[x-row+n-1] = 1, 1, 1
            combination.append((row, x))
            backtrack(row+1)
            combination.pop()
            col[x], diag1[row + x], diag2[x-row+n-1] = 0, 0, 0
    col = [0 for i in range(n)]
    diag1 = [0 for i in range(2*n-1)]
    diag2 = [0 for i in range(2*n-1)]
    backtrack(0)
    return result


def get_combinations_of_queens(n):
    result = []
    combination = []

    def get_queen_alignment(combination):
        res = [["." for i in range(n)] for j in range(n)]
        for x, y in combination:
            res[x][y] = 'Q'
        return [''.join(row) for row in res]

    def backtrack(row):
        if row == n:
            result.append(get_queen_alignment(combination))
            return
        for x in range(n):
            if col[x] or diag1[x+row] or diag2[x-row+n-1]:
                continue
            col[x], diag1[row+x], diag2[x-row+n-1] = 1, 1, 1
            combination.append((row, x))
            backtrack(row+1)
            combination.pop()
            col[x], diag1[row + x], diag2[x-row+n-1] = 0, 0, 0
    col = [0 for i in range(n)]
    diag1 = [0 for i in range(2*n-1)]
    diag2 = [0 for i in range(2*n-1)]
    backtrack(0)
    return result


print(find_no_of_ways(4))
print(find_combinations_of_queens(4))
print(get_combinations_of_queens(4))

