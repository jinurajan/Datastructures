"""
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.
Example 1:

Input: {-4,10,3,7,15}
Output: 4
Explanation: The LIS is {-4,3,7,15}.
"""
def find_LIS_length(nums):
    return find_LIS_length_recursive(nums, 0, -1)

def find_LIS_length_recursive(nums, curr_idx, prev_idx):
    if curr_idx == len(nums):
        return 0
    c1 = 0
    if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
        c1 = 1 + find_LIS_length_recursive(nums, curr_idx+1, curr_idx)

    c2 = find_LIS_length_recursive(nums, curr_idx+1, prev_idx)
    return max(c1, c2)


def find_LIS_length_topdown(nums):
    n = len(nums)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LIS_length_recursive_top_down(dp, nums, 0, -1)

def find_LIS_length_recursive_top_down(dp, nums, curr_idx, prev_idx):
    if curr_idx == len(nums):
        return 0
    c1 = 0
    if dp[curr_idx][prev_idx] == -1:
        if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
            c1 = 1 + find_LIS_length_recursive_top_down(dp, nums, curr_idx+1, curr_idx)
        c2 = find_LIS_length_recursive_top_down(dp, nums, curr_idx+1, prev_idx)
        dp[curr_idx][prev_idx] = max(c1, c2)
    return dp[curr_idx][prev_idx]


def find_LIS_length_bottom_up(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 1
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                max_len = max(max_len, dp[i])
    return max_len



print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
print(find_LIS_length([-4, 10, 3, 7, 15]))

print(find_LIS_length_topdown([4, 2, 3, 6, 10, 1, 12]))
print(find_LIS_length_topdown([-4, 10, 3, 7, 15]))

print(find_LIS_length_bottom_up([4, 2, 3, 6, 10, 1, 12]))
print(find_LIS_length_bottom_up([-4, 10, 3, 7, 15]))
