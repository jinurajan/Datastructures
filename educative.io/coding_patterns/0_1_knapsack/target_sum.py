"""
You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}


sum(s1) - sum(s2) = S
sum(s1) + sum(s2) = sum(num)

sum(s1) - sum(s2) + sum(s1) + sum(s2) = S + sum(num)

2 * sum(s1) = S + sum(num)
sum(s1) = S +sum(num) / 2

Find the count of subsets of the given numbers whose sum is equal to (S + Sum(num)) / 2
"""

def find_target_subsets(num, s):
    total = sum(num)
    if total < s or (s + total) % 2 == 1:
        return False
    return count_subsets(num, (s+total)// 2)

def count_subsets(num, s):
    n = len(num)
    dp =[[0 for _ in range(s+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(1, s+1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] += dp[i-1][j-num[i]]
    return dp[n-1][j]


def find_target_subsets_space_optimized(num, s):
    total = sum(num)
    if total < s or (s + total) % 2 == 1:
        return False
    return count_subsets_optimized(num, (s+total)// 2)

def count_subsets_optimized(num, sum_val):
    n = len(num)
    dp = [0 for x in range(sum_val + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, sum_val + 1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum_val, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]

    return dp[sum_val]





def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))

  print("Total ways: " + str(find_target_subsets_space_optimized([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets_space_optimized([1, 2, 7, 1], 9)))


main()
