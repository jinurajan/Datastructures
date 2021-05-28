"""
Given a number sequence, find the length of its Longest Alternating Subsequence (LAS). A subsequence is considered alternating if its elements are in alternating order.

A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:

{a1 > a2 < a3 } or { a1 < a2 > a3}.
Example 1:

Input: {1,2,3,4}
Output: 2
Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
Example 2:

Input: {3,2,1,4}
Output: 3
Explanation: The LAS are {3,2,4} and {2,1,4}.
Example 3:

Input: {1,3,2,4}
Output: 4
Explanation: The LAS is {1,3,2,4}.
"""

def find_LAS_length(nums):
    return max(find_LAS_length_recursive(nums, -1, 0, True), find_LAS_length_recursive(nums, -1, 0, False))


def find_LAS_length_recursive(nums, prev_idx, curr_idx, is_asc):
    if curr_idx == len(nums):
        return 0
    c1 = 0
    if is_asc:
        if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
            c1 = 1 + find_LAS_length_recursive(nums, curr_idx, curr_idx+1, not is_asc)
    else:
        if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
            c1 = 1 + find_LAS_length_recursive(nums, curr_idx, curr_idx+1, not is_asc)
    c2 = find_LAS_length_recursive(nums, prev_idx, curr_idx+1, is_asc)
    return max(c1, c2)

def find_LAS_length_top_down(nums):
    n = len(nums)
    dp= [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    return max(find_LAS_length_recursive_topdown(dp, nums, -1, 0, True), find_LAS_length_recursive_topdown(dp, nums, -1, 0, False))


def find_LAS_length_recursive_topdown(dp, nums, prev_idx, curr_idx, is_asc):
    if curr_idx == len(nums):
        return 0
    if dp[prev_idx+1][curr_idx][1 if is_asc else 0] == -1:
        c1 = 0
        if is_asc:
            if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
                c1 = 1 + find_LAS_length_recursive_topdown(dp, nums, curr_idx, curr_idx+1, not is_asc)
        else:
            if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
                c1 = 1 + find_LAS_length_recursive_topdown(dp, nums, curr_idx, curr_idx+1, not is_asc)
        c2 = find_LAS_length_recursive_topdown(dp, nums, prev_idx, curr_idx+1, is_asc)
        dp[prev_idx+1][curr_idx][1 if is_asc else 0] = max(c1, c2)
    return dp[prev_idx+1][curr_idx][1 if is_asc else 0]



def find_LAS_length_bottomup(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    max_len = 1
    for i in range(n):
        dp[i][0] = dp[i][1] = 1
        for j in range(i):
            if nums[i] >  nums[j]:
                dp[i][0] = max(dp[i][0], 1+dp[j][1])
                max_len = max(max_len, dp[i][0])
            elif nums[i] < nums[j]:
                dp[i][1] = max(dp[i][1], 1+dp[j][0])
                max_len = max(max_len, dp[i][1])
    return max_len


print(find_LAS_length([1, 2, 3, 4]))
print(find_LAS_length([3, 2, 1, 4]))
print(find_LAS_length([1, 3, 2, 4]))


print(find_LAS_length_top_down([1, 2, 3, 4]))
print(find_LAS_length_top_down([3, 2, 1, 4]))
print(find_LAS_length_top_down([1, 3, 2, 4]))


print(find_LAS_length_bottomup([1, 2, 3, 4]))
print(find_LAS_length_bottomup([3, 2, 1, 4]))
print(find_LAS_length_bottomup([1, 3, 2, 4]))
