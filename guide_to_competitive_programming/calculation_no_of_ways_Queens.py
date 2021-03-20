"""
calculating the number of ways n queens can be placed on an n by n chessboard so that no two queens attack each other
"""




def find_no_of_ways(n):
    count = 0
    def search(y):
        nonlocal count
        if y == n:
            count += 1
            return
        for x in range(n):
            if col[x] or diag[x+y] or diag1[x-y+n-1]:
                continue
            col[x] = diag[x+y] = diag1[x-y+n-1] = 1
            search(y+1)
            col[x] = diag[x + y] = diag1[x - y + n - 1] = 0

    col = [0] * n
    diag = [0] * (2*n-1)
    diag1 = [0] * (2*n-1)
    search(0)
    return count

print(find_no_of_ways(4))
print(find_no_of_ways(8))
print(find_no_of_ways(16))
