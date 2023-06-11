"""
Given a number n, calculate the corresponding Tribonacci number. The Tribonacci sequence T n is defined as
T0 = 0
T1 = 1
T2 = 1
T n+3 = Tn + Tn+1 + Tn+2 for n >= 0
"""

def find_tribonacci(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return find_tribonacci(n-1) + find_tribonacci(n-2) + find_tribonacci(n-3) 

# with memoization

from functools import lru_cache

@lru_cache(maxsize=None)
def find_tribonacci(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return find_tribonacci(n-1) + find_tribonacci(n-2) + find_tribonacci(n-3) 


def find_tribonacci(n):
    # topdown
    if n < 3:
        return 1 if n else 0
    dp1, dp2, dp3 = 0, 1, 1

    for i in range(n-2):
        dp1, dp2, dp3 = dp2, dp3, dp1 + dp2 + dp3
    
    return dp3