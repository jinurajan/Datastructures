
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import ceil, sqrt

def solution(A, B):
    # write your code in Python 3.6
    """
    B is the highest number and the
    max integer cannot be more than square root of B

    Complexity : O(squareroot(B))
    """
    count = 0
    result_range = range(A, B + 1)
    upper_limit = int(ceil(sqrt(B)))
    for i in range(upper_limit):
        if i * (i + 1) in result_range:
            count = count + 1

    return count


# print solution(6, 20)
# print solution(21, 29)
# print solution(1, 2)
# print solution(0, 1)
print solution(1, 10)