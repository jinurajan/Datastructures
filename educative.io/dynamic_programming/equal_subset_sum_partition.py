"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equa

Find a subset of the given numbers that has a total sum of S/2".
"""


def can_partition(num):
    # Time complexity = O(2 raised to N)
    # Space complexity = O(N) for recursive stack
    s = sum(num)
    if s % 2 == 1:
        return False
    return can_paritition_recursive(num, s/2, 0)

def can_paritition_recursive(num, sum_val, curr_index):
    if sum_val == 0:
        return True
    n = len(num)
    if n == 0 or curr_index >= n:
        return False
    if num[curr_index] <= sum_val:
        if can_paritition_recursive(num, sum_val-num[curr_index], curr_index+1):
            return True
    return can_paritition_recursive(num, sum_val, curr_index+1)


def can_partition_dp_top_down(num):
    """
    Time complexity: O (N *S/2) S is the total sum of all numbers
    """
    s = sum(num)
    if s % 2 == 1:
        return False
    dp = [[-1 for i in range(int(s/2)+1)] for j in range(len(num))]

    def dp_recursive(num, sum_val, index):
        if sum_val == 0:
            return 1
        n = len(num)
        if n == 0 or index >= n:
            return 0
        if dp[index][sum_val] == -1:
            if num[index] <= sum_val:
                if dp_recursive(num, sum_val - num[index], index+1) == 1:
                    dp[index][sum_val] = 1
                    return 1
            dp[index][sum_val] = dp_recursive(num, sum_val, index+1)
        return dp[index][sum_val]

    return True if dp_recursive(num, int(s / 2), 0) == 1 else False


def can_partition_dp_bottom_up(num):
    """
    Time complexity = O(N * S) where s is the half of sum of nums
    Space Complexity = O (N * S)
    """
    s = sum(num)
    if s % 2 == 1:
        return False
    n = len(num)
    s = int(s/2)+1
    dp = [[False for i in range(s)] for j in range(n)]
    for j in range(s):
        dp[0][j] =  num[0] == j
    for i in range(1, n):
        for j in range(1, s):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[-1][-1]



print(can_partition([1, 2, 3, 4]))
print(can_partition_dp_top_down([1, 2, 3, 4]))
print(can_partition_dp_bottom_up([1, 2, 3, 4]))