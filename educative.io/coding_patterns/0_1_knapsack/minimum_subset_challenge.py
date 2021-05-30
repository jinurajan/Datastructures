"""
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""
def can_partition(num):
  return can_partition_recursive(num, 0, 0, 0)

def can_partition_recursive(num, index, s1, s2):
    if index == len(num):
        return abs(s1-s2)
    diff1 = can_partition_recursive(num, index+1, s1+num[index], s2)
    diff2 = can_partition_recursive(num, index+1, s1, s2+num[index])
    return min(diff1, diff2)

def can_partition_topdown(num):
    n = len(num)
    s = sum(num)
    dp = [[-1 for _ in range(s+1)] for _ in range(n)]
    return can_partition_recursive_topdown(dp, num, 0, 0, 0)

def can_partition_recursive_topdown(dp, num, index, s1, s2):
    if index == len(num):
        return abs(s1-s2)
    if dp[index][s1] == -1:
        diff1 = can_partition_recursive_topdown(dp,num, index + 1, s1 + num[index], s2)
        diff2 = can_partition_recursive_topdown(dp, num, index + 1, s1, s2 + num[index])
        dp[index][s1] = min(diff2, diff1)
    return dp[index][s1]

def can_partition_bottomup(num):
    n = len(num)
    sum_val = sum(num)
    s = int(s/2)
    dp = [[False for _ in range(s+1)] for _ in range(n)]
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
    sum2 = sum_val - sum1
    return abs(sum2-sum1)




def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))
  print("------")
  print("Can partition: " + str(can_partition_topdown([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition_topdown([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition_topdown([1, 3, 100, 4])))
  print("------")
  print("Can partition: " + str(can_partition_bottomup([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition_bottomup([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition_bottomup([1, 3, 100, 4])))



main()