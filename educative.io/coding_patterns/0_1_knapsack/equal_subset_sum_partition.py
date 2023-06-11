"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
"""



def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    return can_partition_recursive(num, 0, s/2)

def can_partition_recursive(num, index, sum_val):
    if sum_val == 0:
        return True
    n = len(num)
    if n == 0 or index >= n:
        return False
    if num[index] <= sum_val:
        if can_partition_recursive(num, index+1, sum_val-num[index]):
            return True
    return can_partition_recursive(num, index+1, sum_val)


def can_partition_topdown(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    n = len(num)
    dp = [[-1 for _ in range(int(s/2)+1)] for _ in range(n)]
    return can_partition_recursive_topdown(dp, num, 0, int(s/2))

def can_partition_recursive_topdown(dp, num, index, sum_val):
    if sum_val == 0:
        return True
    n = len(num)
    if n == 0 or index >= n:
        return False
    if dp[index][sum_val] == -1:
        if num[index] <= sum_val:
            dp[index][sum_val] = can_partition_recursive_topdown(dp, num, index+1, sum_val-num[index]):
        else:
            dp[index][sum_val] = can_partition_recursive_topdown(dp, num, index+1, sum_val)
    return dp[index][sum_val]


def can_partition_bottomup(num):
    s = sum(num)
    if s % 2 == 1:
        return False
    n = len(num)
    s = int(s/2)
    dp = [[False for _ in range(s+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True

    for j in range(1, s+1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][s]








def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
    print("")

    print("Can partition: " + str(can_partition_topdown([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_topdown([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_topdown([2, 3, 4, 6])))

    print("")

    print("Can partition: " + str(can_partition_bottomup([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_bottomup([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_bottomup([2, 3, 4, 6])))


main()