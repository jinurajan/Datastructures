"""
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
Example 2: #
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}
Example 3: #
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
"""

def can_partition(num, sum):
  # TODO: Write your code here
  return can_partition_recursive(num, sum, 0, 0)

def can_partition_recursive(num, sum_val, index, s):
  if index >= len(num):
    return False
  if sum_val == s:
    return True
  c1 = 0
  if num[index] <= sum_val:
    c1 = can_partition_recursive(num, sum_val, index+1, s+num[index])
  c2 = can_partition_recursive(num, sum_val, index+1, s)
  return c1 or c2


def can_partition_bottomup(num, sum):
    n = len(num)
    dp = [[False for _ in range(sum+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    for j in range(sum+1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, sum+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][sum]


def can_partition_bottomup_optimized(num, sum):
    n = len(num)
    dp = [False for _ in range(sum+1)]
    dp[0] = True
    for j in range(sum+1):
        dp[j] = num[0] == j
    for i in range(1, n):
        for j in range(sum, -1, -1):
            if not dp[j] and j >= num[i]:
                dp[j] = dp[j-num[i]]
    return dp[sum]




def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
  print("------")
  print("Can partition: " + str(can_partition_bottomup([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition_bottomup([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition_bottomup([1, 3, 4, 8], 6)))
  print("------")
  print("Can partition: " + str(can_partition_bottomup_optimized([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition_bottomup_optimized([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition_bottomup_optimized([1, 3, 4, 8], 6)))


main()

