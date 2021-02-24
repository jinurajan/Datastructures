"""
Backtracking
calculate the number of paths in an n by n grid from the upper-left corner to the lower-right corner such that the path visits each square exactly once
"""
from time import time

def find_no_of_paths(m, n):
    count = 0
    def backtrack(x, y):
        if x < 0 or x >= m or y < 0 or y >= m:
            return
        nonlocal count
        if (x, y) == (m-1, n-1):
            count += 1
            return
        for idx, idy in [(0, 1), (1, 0)]:
            backtrack(x+idx, y+idy)

    backtrack(0, 0)
    return count


def find_no_of_paths_1(m, n):
    count = 0
    def backtrack(x, y):
        if x < 0 or x >= m or y <0 or y >= n:
            return
        nonlocal count
        if (x, y) == (m-1, n-1):
            count += 1
            return
        backtrack(x, y+1)
        backtrack(x+1, y)

    backtrack(0, 0)
    return count

def find_no_of_paths_2(m, n):
    if m == 1 or n == 1:
        return 1
    return find_no_of_paths_2(m-1, n) + find_no_of_paths_2(m, n-1)


mem = {}

def find_no_of_paths_3(m, n):
    if (m,n) in mem:
        return mem[(m, n)]
    else:
        if m == 1 or n == 1:
            mem[(m,n)] = 1
        res1 = find_no_of_paths_2(m-1, n)
        res2 = find_no_of_paths_2(m, n-1)
        if (m-1,n) not in mem:
            mem[(m-1, n)] = res1
        if (m, n-1) not in mem:
            mem[(m, n-1)] = res2
    return res1 + res2

def find_no_of_paths_4(m, n):
    "using dp O(mn)"
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0] = [1 for i in range(n)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(1, m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

def find_no_of_paths_5(m, n):
    "using dp using O(n)"
    dp = [1 for i in range(n)]
    for i in range(m-1):
        for j in range(1,n):
            dp[j] += dp[j-1]
    return dp[n-1]

def find_no_of_paths_6(m, n):
    """ using combinatorics
        total number = (m-1 + n-1)! /(m-1 )! (n-1)!
        m+n-2 C n-1= (m+n-2)! (m-1)! (n-1)!
    """
    path = 1
    for i in range(n, m+n-1):
        path *= i
        path //= i-n+1
    return path




current_time = time()
print(find_no_of_paths(10, 10))
print(time()-current_time)

current_time = time()
print(find_no_of_paths_1(10, 10))
print(time()-current_time)

current_time = time()
print(find_no_of_paths_2(10, 10))
print(time()-current_time)

current_time = time()
print(find_no_of_paths_3(10, 10))
print(time()-current_time)

current_time = time()
print(find_no_of_paths_4(10, 10))
print(time()-current_time)

current_time = time()
print(find_no_of_paths_5(10, 10))
print(time()-current_time)


current_time = time()
print(find_no_of_paths_6(10, 10))
print(time()-current_time)