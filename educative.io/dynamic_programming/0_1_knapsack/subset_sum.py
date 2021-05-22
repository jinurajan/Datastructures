"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
"""


def can_partition(num, sum_val):
    if sum_val == 0:
        return True
    n = len(num)
    dp = [[False for i in range(sum_val+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
    for j in range(1, sum_val+1):
        dp[0][j] = True if num[0] == j else False
    for i in range(1, n):
        for j in range(1, sum_val+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                print(i, j, j-num[i])
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[-1][-1]




num = [1,2, 3,7]
sum_val = 10
num = [5,-7,3,5]
sum_val = 6
print(can_partition(num, sum_val))
print(can_partition(num, 11))
# print(can_partition(num, 3))