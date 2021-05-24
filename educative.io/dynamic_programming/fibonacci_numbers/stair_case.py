"""
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

Example 1:

Number of stairs (n) : 3
Number of ways = 4
Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}
Example 2:

Number of stairs (n) : 4
Number of ways = 7
Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
{2,2}, {1,3}, {3,1}
"""

def count_ways(n):
    """
    time: O( 3 raised to n)
    """
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

def count_ways_top_down(n):
    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = 1,1
    dp[2] = 2
    def count_ways(n):
        if dp[n] != 0:
            return dp[n]
        dp[n] = count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
        return dp[n]
    return count_ways(n)

def count_ways_bottom_up(n):
    dp = [0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 1,1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[-1]

def count_ways_mem_optimized(n):
    n1, n2, n3, tmp = 1, 1, 2, 0
    for i in range(3, n+1):
        n1, n2, n3 = n2, n3, n1+n2+n3
    return n3

print(count_ways(3))
print(count_ways(4))
print(count_ways(5))

print(count_ways_top_down(3))
print(count_ways_top_down(4))
print(count_ways_top_down(5))

print(count_ways_bottom_up(3))
print(count_ways_bottom_up(4))
print(count_ways_bottom_up(5))

print(count_ways_mem_optimized(3))
print(count_ways_mem_optimized(4))
print(count_ways_mem_optimized(5))