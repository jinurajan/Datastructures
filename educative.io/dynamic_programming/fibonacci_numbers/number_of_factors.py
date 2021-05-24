"""
Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

Example 1:

n : 4
Number of ways = 4
Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}
Example 2:

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
{1,4}, {4,1}
"""

def count_ways(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2
    return count_ways(n-1) + count_ways(n-3) + count_ways(n-4)

def count_ways_top_down(n):
    dp =[0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 1, 1, 1
    dp[3] = 2

    def count(n):
        if dp[n] != 0:
            return dp[n]
        dp[n] = count(n-1) + count(n-3) + count(n-4)
        return dp[n]
    return count(n)

def count_ways_bottom_up(n):
    dp =[0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 1, 1, 1
    dp[3] = 2
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[-1]

print(count_ways(4))
print(count_ways(5))
print(count_ways(6))

print(count_ways_top_down(4))
print(count_ways_top_down(5))
print(count_ways_top_down(6))

print(count_ways_bottom_up(4))
print(count_ways_bottom_up(5))
print(count_ways_bottom_up(6))