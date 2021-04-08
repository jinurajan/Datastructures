"""

"""

def number_of_queens(n):
    col = [0] * n
    l_diag = [0] *(2*n+1)
    anti_diag = [0] * (2*n+1)
    count = 0
    def search(y):
        nonlocal count
        if y == n:
            count += 1
            return
        for x in range(n):
            if col[x] or l_diag[x+y] or anti_diag[x-y+n-1]:
                continue
            col[x] = l_diag[x+y] = anti_diag[x-y+n-1] = 1
            search(y+1)
            col[x] = l_diag[x+y] = anti_diag[x-y+n-1] = 0
    search(0)
    return count


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        l_diag = [0] * (2 * n + 1)
        anti_diag = [0] * (2 * n + 1)
        result = []

        def format_queens(positions):
            res = [['.' for i in range(n)] for j in range(n)]
            for x, y in positions:
                res[x][y] = 'Q'
            return ["".join(r) for r in res]

        def search(y):
            if y == n:
                result.append(format_queens(positions[:]))
                return
            for x in range(n):
                if cols[x] or l_diag[x + y] or anti_diag[x - y + n - 1]:
                    continue
                cols[x] = l_diag[x + y] = anti_diag[x - y + n - 1] = 1
                positions.append((x, y))
                search(y + 1)
                cols[x] = l_diag[x + y] = anti_diag[x - y + n - 1] = 0
                positions.pop()

        positions = []
        search(0)
        return result


print(number_of_queens(4))
