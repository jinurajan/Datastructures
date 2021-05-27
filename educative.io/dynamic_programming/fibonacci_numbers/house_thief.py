"""
There are n houses built in a line. A thief wants to steal the maximum possible money from these houses. The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can steal without alerting the security system.

Example 1:

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
Example 2:

Input: {2, 10, 14, 8, 1}
Output: 18
Explanation: The thief should steal from houses 10 + 8

"""


def find_max_steal(wealth):
    return find_max_steal_recursive(wealth, 0, len(wealth))


def find_max_steal_recursive(wealth, index, n):
    if index >= n:
        return 0

    p1 = wealth[index] + find_max_steal_recursive(wealth, index + 2, n)

    p2 = find_max_steal_recursive(wealth, index + 1, n)

    return max(p1, p2)

def find_max_steal_top_bottom(wealth):
    n = len(wealth)
    dp = [0 for i in range(n)]

    def find_max_steal(index):
        if index >= n:
            return 0
        if dp[index] == 0:
            p1 = wealth[index] + find_max_steal(index+2)
            p2 = find_max_steal(index+1)
            dp[index] = max(p1, p2)
        return dp[index]

    return find_max_steal(0)

def find_max_steal_bottom_up(wealth):
    n = len(wealth)
    dp = [0 for i in range(n)]
    dp[0] = wealth[0]
    dp[1] = wealth[1]

    for i in range(2, n):
        dp[i] = max(wealth[i]+ dp[i-2], dp[i-1])
    return dp[-1]


def find_max_steal_mem_optimized(wealth):
    n = len(wealth)
    n1, n2 = wealth[0], wealth[1]
    for i in range(2, n):
        n1, n2 = n2, max(wealth[i]+n1, n2)
    return n2


# print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
# print(find_max_steal([2, 10, 14, 8, 1]))

print(find_max_steal_top_bottom([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal_top_bottom([2, 10, 14, 8, 1]))


print(find_max_steal_bottom_up([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal_bottom_up([2, 10, 14, 8, 1]))

print(find_max_steal_mem_optimized([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal_mem_optimized([2, 10, 14, 8, 1]))