"""
Count of Subset Sum (hard) #
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

"""


def count_subsets(num, sum):
    return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, index):
    if sum == 0:
        return 1
    if index >= len(num):
        return 0
    s1 = 0
    if num[index] <= sum:
        s1 = count_subsets_recursive(num, sum-num[index], index + 1)
    s2 = count_subsets_recursive(num, sum, index + 1)
    return s1 + s2

def count_subsets_topdown(num, sum):
    dp =[[-1 for _ in range(sum+1)] for _ in range(len(num))]
    return count_subsets_recursive_topdown(dp, num, sum, 0)

def count_subsets_recursive_topdown(dp, num, sum, index):
    if sum == 0:
        return 1
    if index >= len(num):
        return 0
    if dp[index][sum] == -1:
        s1 = 0
        if num[index] <= sum:
            s1 = count_subsets_recursive_topdown(dp, num, sum-num[index], index+1)
        s2 = count_subsets_recursive_topdown(dp, num, sum, index+1)
        dp[index][sum] = s1 + s2
    return dp[index][sum]

def count_subsets_bottomup(num, sum):
    n = len(num)
    dp =[[-1 for _ in range(sum+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(1, sum+1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(1, n):
        for j in range(1, sum+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] += dp[i-1][j-num[i]]
    return dp[n-1][sum]

def count_subsets_bottomup_optimized(num, sum):
    n = len(num)
    dp = [0 for _ in range(sum+1)]
    dp[0] = 1
    for s in range(1, sum+1):
        dp[s] = 1 if num[0] == s else 0
    for i in range(1, n):
        for j in range(sum, -1, -1):
            if j >= num[i]:
                dp[j] += dp[j-num[i]]
    return dp[-1]




def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    print("-----")
    print("Total number of subsets " + str(count_subsets_topdown([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_topdown([1, 2, 7, 1, 5], 9)))
    print("-----")
    print("Total number of subsets " + str(count_subsets_bottomup([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_bottomup([1, 2, 7, 1, 5], 9)))
    print("-----")
    print("Total number of subsets " + str(count_subsets_bottomup_optimized([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_bottomup_optimized([1, 2, 7, 1, 5], 9)))


main()

