



def no_of_ways_queen(n):
    count = 0

    diag1 = [0] * ((2*n)-1)
    diag2 = [0] * ((2*n)-1)
    col = [0] * n

    def backtrack(y):
        nonlocal count
        if y == n:
            count += 1
            return
        else:
            for x in range(n):
                if col[x] or diag1[x+y] or diag2[y-x+n-1]:
                    continue
                col[x], diag1[x+y], diag2[y-x+n-1] = 1,1,1
                backtrack(y+1)
                col[x], diag1[x+y], diag2[y-x+n-1] = 0,0,0
    backtrack(0)
    return count


print(no_of_ways_queen(4))
print(no_of_ways_queen(6))
print(no_of_ways_queen(7))
print(no_of_ways_queen(8))            
