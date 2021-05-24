"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.


Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Let’s try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod into two pieces of length ‘2’ and one piece of length ‘1’.
"""


def solve_rod_cutting(lengths, prices, n):
    return solve_rod_cutting_recursive(lengths, prices, n, 0)

def solve_rod_cutting_recursive(lengths, prices, capacity, index):
    if capacity <= 0 or index >= len(lengths):
        return 0
    p1, p2 = 0, 0
    if lengths[index] <= capacity:
        p1 = prices[index] + solve_rod_cutting_recursive(lengths, prices, capacity-lengths[index], index)
    p2 = solve_rod_cutting_recursive(lengths, prices, capacity, index+1)
    return max(p1, p2)


def solve_rod_cutting_bottom_up(lengths, prices, n):
    l = len(lengths)
    if n <= 0 or l == 0 or len(prices) != len(lengths):
        return 0
    dp = [[0 for i in range(n+1)] for j in range(l)]
    for i in range(l):
        for j in range(1, n+1):
            p1, p2 = 0, 0
            if j >= lengths[i]:
                p1 = prices[i]+dp[i][j-lengths[i]]
            if i > 0:
                p2 = dp[i-1][j]
            dp[i][j] = max(p1, p2)
    return dp[l-1][n]



print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
print(solve_rod_cutting_bottom_up([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
