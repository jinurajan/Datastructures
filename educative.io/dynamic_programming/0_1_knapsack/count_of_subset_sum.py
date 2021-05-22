"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.


"""


def count_subsets(num, sum_val):
    return count_subsets_recursive(num, sum_val, 0)

def count_subsets_recursive(num, sum_val, index):
    if sum_val == 0:
        return 1
    n = len(num)
    if index >= n:
        # boundary condition
        return 0
    s1, s2 = 0, 0
    if num[index] <= sum_val:
        s1 = count_subsets_recursive(num, sum_val-num[index], index+1)
    s2 = count_subsets_recursive(num, sum_val, index+1)
    return s1 + s2


def count_subsets_top_down(num, sum_val):
    if sum_val == 0:
        return 1
    n = len(num)
    dp = [[-1 for i in range(sum_val+1)] for j in range(n)]

    def count_subsets_recursive_top_down(num, sum_val, index):
        if sum_val == 0:
            return 1
        n = len(num)
        if index >= n:
            return 0
        if dp[index][sum_val] == -1:
            s1, s2 = 0, 0
            s1 = count_subsets_recursive_top_down(num, sum_val-num[index], index+1)
            s2 = count_subsets_recursive_top_down(num, sum_val, index+1)
            dp[index][sum_val] =  s1 + s2
        return dp[index][sum_val]

    return count_subsets_recursive_top_down(num, sum_val, 0)



def count_subsets_bottom_up(num, sum_val):
    if sum_val == 0:
        return 1
    n = len(num)
    dp = [[0 for i in range(sum_val+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for s in range(1, sum_val+1):
        dp[0][s] = 1 if num[0] == s else 0

    for i in range(1, n):
        for j in range(1, sum_val+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] += dp[i-1][j-num[i]]
    return dp[-1][-1]


def count_subsets_oned(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]





num = [1, 1, 2, 3]
sum_val = 4
print(count_subsets(num, sum_val))
print(count_subsets_top_down(num, sum_val))
print(count_subsets_bottom_up(num, sum_val))
print(count_subsets_oned(num, sum_val))