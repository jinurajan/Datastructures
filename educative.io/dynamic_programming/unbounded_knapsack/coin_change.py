"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1}
  2. {1,1,1,2}
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
"""

def count_change(denominations, total):
    return count_change_recursive(denominations, total, 0)

def count_change_recursive(denominations, total, index):
    if total == 0:
        return 1
    n = len(denominations)
    if n == 0 or index >= n:
        return 0
    s1  = 0
    if denominations[index] <= total:
        s1 = count_change_recursive(denominations, total-denominations[index], index)
    s2 = count_change_recursive(denominations, total, index+1)
    return s1 + s2


def count_change_topdown(denominations, total):
    if not denominations or not total:
        return 0
    n = len(denominations)
    dp = [[-1 for i in range(total+1)] for j in range(n)]

    def count_change_recursive(sum_val, index):
        if sum_val == 0:
            return 1
        if index >= n:
            return 0
        if dp[index][sum_val] == -1:
            s1 = 0
            if denominations[index] <= sum_val:
                s1 = count_change_recursive(sum_val-denominations[index], index)
            s2 = count_change_recursive(sum_val, index+1)
            dp[index][sum_val] = s1 + s2
        return dp[index][sum_val]
    return count_change_recursive(total, 0)


def count_change_bottomup(denominations, total):
    if not denominations or not total:
        return 0
    n = len(denominations)
    dp = [[0 for i in range(total + 1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, total+1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            if j >= denominations[i]:
                dp[i][j] +=  dp[i][j-denominations[i]]
    return dp[-1][-1]


print(count_change([1, 2, 3], 5))
print(count_change_topdown([1, 2, 3], 5))
print(count_change_bottomup([1, 2, 3], 5))
