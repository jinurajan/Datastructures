"""
Find longest Increasing subsequence
"""
from bisect import bisect_left


def find_longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def find_longest_increasing_subsequence_1(nums):
    LIS = []
    for n in nums:
        if not LIS or n > LIS[-1]:
            LIS.append(n)
        else:
            pos = bisect_left(LIS, n, 0, len(LIS))
            LIS[pos] = n
    return len(LIS)




nums = [6, 2, 5, 1, 7, 4, 8, 3]
print(find_longest_increasing_subsequence(nums))
print(find_longest_increasing_subsequence_1(nums))