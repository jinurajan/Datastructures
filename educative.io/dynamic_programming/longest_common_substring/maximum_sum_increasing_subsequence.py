"""
Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

Example 1:

Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increaseing sequence is {4,6,10,12}.
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
Example 2:

Input: {-4,10,3,7,15}
Output: 25
Explanation: The increaseing sequences are {10, 15} and {3,7,15}
"""

def find_MSIS(nums):
    n = len(nums)
    return find_MSIS_recursive(nums, 0, -1, 0)

def find_MSIS_recursive(nums, curr_idx, prev_idx, s):
    if curr_idx == len(nums):
        return s
    s1 = s
    if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
        s1 = find_MSIS_recursive(nums, curr_idx+1, curr_idx, s+nums[curr_idx])
    s2 = find_MSIS_recursive(nums, curr_idx+1, prev_idx, s)
    return max(s1, s2)

def find_MSIS_topdown(nums):
    n = len(nums)
    dp = {}
    return find_MSIS_recursive_topdown(dp, nums, 0, -1, 0)

def find_MSIS_recursive_topdown(dp, nums, curr_idx, prev_idx, s):
    if curr_idx == len(nums):
        return s
    key = str(curr_idx) + "-" + \
                    str(prev_idx) + "-" + str(s)
    if key not in dp:
        s1 = s
        if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
            s1 = find_MSIS_recursive_topdown(dp, nums, curr_idx + 1, curr_idx, s + nums[curr_idx])
        s2 = find_MSIS_recursive_topdown(dp, nums, curr_idx + 1, prev_idx, s)
        dp[key] = max(s1, s2)
    return dp[key]


def find_MSIS_bottomup(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
    max_sum = max(max_sum, dp[i])
    return max_sum




# print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
print(find_MSIS([-4, 10, 3, 7, 15]))

# print(find_MSIS_topdown([4, 1, 2, 6, 10, 1, 12]))
print(find_MSIS_topdown([-4, 10, 3, 7, 15]))

# print(find_MSIS_bottomup([4, 1, 2, 6, 10, 1, 12]))
# print(find_MSIS_bottomup([-4, 10, 3, 7, 15]))