"""
Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 2
Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.
Example 2:

Input: {-4,10,3,7,15}
Output: 1
Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.
Example 3:

Input: {3,2,1,0}
Output: 3
Explanation: Since the elements are in reverse order, we have to delete all except one to get a
sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}
"""


def find_minimum_deletions(nums):
    return len(nums) - find_LIS(nums)

def find_LIS(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 1
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = 1 + dp[j]
            max_len = max(max_len, dp[i])
    return max_len

print(find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]))
print(find_minimum_deletions([-4, 10, 3, 7, 15]))
print(find_minimum_deletions([3, 2, 1, 0]))
