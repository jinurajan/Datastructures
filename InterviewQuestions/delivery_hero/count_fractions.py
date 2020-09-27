"""
Count the number of occurences of the fraction
"""
from collections import defaultdict

def solution1(X, Y):
    """
    1. len(X)) == len(Y) 
    2. x values start from 0 and y values start from 0
    no need to handle zero division error
    Below Solution requires big amount of memory if array length is larger
    """
    if not X and not Y:
        return 0
    nums = [x/float(y) for x, y in zip(X, Y)]
    return max(nums.count(n) for n in nums)


from collections import defaultdict

GCD_MEM ={}

def solution(X, Y):
    """
    Idea is to store the numerator and denominator in a hash and increment
    the counter
    
    Space Complexity = O(N) worst case if all fractions are different
    O(K) if there are K fractions present
    
    Time Complexity = O(N) since single iteration for the array
    """
    if not X and not Y:
        return 0
    hash_set = defaultdict(int)
    max_val = 0
    count = 0
    for i in range(len(X)):
        gcd_val = gcd(X[i], Y[i])
        n = X[i] // gcd_val
        d = Y[i] // gcd_val
        hash_set[(n, d)] += 1
        if hash_set[(n, d)] > max_val:
            max_val = hash_set[(n, d)]
    return max_val


def gcd(x, y):
    """
    Using memoization here to avoid recomputation
    """
    if (x, ) in GCD_MEM:
        return GCD_MEM[(x, y)]
    if y == 0:
        return x
    r = gcd(y, x % y)
    GCD_MEM[(x,y)] = r
    return r



X = [1,2,3,4,0]
Y = [2,3,6,8,4]

# X = range(2000000)
# Y = range(1, 2000001)
X = [1]
Y = [2]
print solution(X, Y)
# print solution1(X, Y)