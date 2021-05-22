"""
Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where the minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
"""


def can_partition(num):
    n = len(num)
    """
    Time complexity : O(2 raised to N)
    space Complexity: O(N) for recursion
    """
    return can_partition_recursive(num, 0, 0, 0)


def can_partition_recursive(num, index, sum1, sum2 ):
    if index == len(num):
        # reached at the end
        return abs(sum1-sum2)
    diff1 = can_partition_recursive(num, index+1, sum1+num[index], sum2)

    diff2 = can_partition_recursive(num, index+1, sum1, sum2+num[index])
    return min(diff1, diff2)


def can_partition_top_down(num):
    if not num:
        return 0
    n = len(num)
    s = sum(num)
    dp =[[-1 for i in range(s+1)]for j in range(n)]

    def can_partition_recursive_top_down(index, sum1, sum2):
        if index == n:
            return abs(sum1-sum2)
        if dp[index][sum1] == -1:
            dp[index][sum1] = min(
            can_partition_recursive_top_down(index + 1, sum1+num[index], sum2),
            can_partition_recursive_top_down(index + 1, sum1, sum2+num[index]))
        return dp[index][sum1]
    return can_partition_recursive_top_down(0, 0, 0)

def can_partition_bottom_up(num):
    if not num:
        return 0
    n = len(num)
    sum_val = sum(num)
    # we need to find the subset with sum closest to s/2
    s = int(sum_val/2) + 1
    dp = [[False for i in range(s + 1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    for j in range(s+1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    sum1 = 0
    for i in range(s, -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break
    sum2 = sum_val-sum1
    return abs(sum2 - sum1)











num = [1, 2, 3, 9]
print(can_partition(num))
print(can_partition_top_down(num))
print(can_partition_bottom_up(num))
