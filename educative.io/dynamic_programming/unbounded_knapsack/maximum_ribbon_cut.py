"""
Maximum Ribbon Cut
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
Example 3:

n: 13
Ribbon Lengths: {3,5,7}
Output: 3
Explanation: Ribbon pieces will be {3,3,7}.
Problem Statement #
Given a number array to represent possible ribbon lengths and a total ribbon length ‘n,’ we need to find the maximum number of pieces that the ribbon can be cut into.
"""
import math

def count_ribbon_pieces(ribbonLengths, total):
    """
    time : O(2 raised to N + T) where T is total and N is number of ribbonlengths
    Space: O(N+T)
    """
    maxPieces = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
    return -1 if maxPieces == -math.inf else maxPieces

def count_ribbon_pieces_recursive(ribbonLengths, total, index):
    if total == 0:
        return 0
    n = len(ribbonLengths)
    if n == 0 or index >= n:
        return -math.inf
    c1 = -math.inf
    if ribbonLengths[index] <= total:
        c1 = count_ribbon_pieces_recursive(ribbonLengths, total-ribbonLengths[index], index)
        if c1 != -math.inf:
            c1 += 1
    c2 = count_ribbon_pieces_recursive(ribbonLengths, total, index+1)
    return max(c1, c2)

def count_ribbon_pieces_bottom_up(ribbonLengths, total):
    """
    Time = O(N * T)
    Space = O(N * T)
    """
    n = len(ribbonLengths)
    dp =[[-math.inf for i in range(total+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(1, total+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= ribbonLengths[i]:
                dp[i][j] = max(dp[i][j], 1+dp[i][j-ribbonLengths[i]])
    return -1 if dp[n-1][total] == -math.inf else dp[n-1][total]



print(count_ribbon_pieces([2, 3, 5], 5))
print(count_ribbon_pieces([2, 3], 7))
print(count_ribbon_pieces([3, 5, 7], 13))
print(count_ribbon_pieces([3, 5], 7))


print(count_ribbon_pieces_bottom_up([2, 3, 5], 5))
print(count_ribbon_pieces_bottom_up([2, 3], 7))
print(count_ribbon_pieces_bottom_up([3, 5, 7], 13))
print(count_ribbon_pieces_bottom_up([3, 5], 7))