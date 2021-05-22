"""
Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

Example 1: #
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
"""



def count_number_of_ways_to_compute(num, s):
    if any(i < 1 for i in num):
        return -1
    total_sum = sum(num)
    if total_sum < s or (s+total_sum) % 2 == 1:
        return 0
    return count_number_of_ways(num, int((s+total_sum)/ 2))


def count_number_of_ways(num, s):
    n = len(num)
    dp = [[0 for i in range(s+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(1, s+1):
        dp[0][j] = 1 if num[0]== j else 0
    for i in range(1, n):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] += dp[i-1][j-num[i]]
    return dp[n-1][s]


def count_number_of_ways_to_compute_oned(num, s):
    if any(i < 1 for i in num):
        return -1
    total_sum = sum(num)
    if total_sum < s or (s+total_sum) % 2 == 1:
        return 0
    return count_number_of_ways_oned(num, int((s+total_sum)/ 2))


def count_number_of_ways_oned(num, sum_val):
  n = len(num)
  dp = [0 for x in range(sum_val+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum_val+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum_val, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum_val]


print(count_number_of_ways_to_compute([1, 2, 7, 1], 9))
print(count_number_of_ways_to_compute([1, 1, 2, 3], 1))

print(count_number_of_ways_to_compute_oned([1, 2, 7, 1], 9))
print(count_number_of_ways_to_compute_oned([1, 1, 2, 3], 1))