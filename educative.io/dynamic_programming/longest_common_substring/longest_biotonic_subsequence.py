"""
Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LBS is {2,3,6,10,1}.
Example 2:

Input: {4,2,5,9,7,6,10,3,1}
Output: 7
Explanation: The LBS is {4,5,9,7,6,3,1}.
"""

def find_LBS_length(nums):
    max_len = 0
    for i in range(len(nums)):
        c1 = find_LDS_length(nums, i, -1)
        c2 = find_LDS_length_rev(nums, i, -1)
        max_len = max(max_len, c1+c2 -1)
    return max_len

def find_LDS_length(nums, curr_idx, prev_idx):
    if curr_idx == len(nums):
        return 0
    c1 = 0
    if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
        c1 = 1+ find_LDS_length(nums, curr_idx+1, curr_idx)

    c2 = find_LDS_length(nums, curr_idx+1, prev_idx)
    return max(c1, c2)

def find_LDS_length_rev(nums, curr_idx, prev_idx):
    if curr_idx < 0:
        return 0
    c1 = 0
    if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
        c1 = 1+ find_LDS_length_rev(nums, curr_idx-1, curr_idx)

    c2 = find_LDS_length_rev(nums, curr_idx-1, prev_idx)
    return max(c1, c2)


def find_LBS_length_topdown(nums):
    n = len(nums)
    lds = [[-1 for _ in range(n)] for _ in range(n)]
    lds_rev = [[-1 for _ in range(n)] for _ in range(n)]
    max_len = 0
    for i in range(n):
        c1 = find_LDS_length_topdown(lds, nums, i, -1)
        c2 = find_LDS_length_topdown_rev(lds_rev, nums, i, -1)
        max_len = max(max_len, c1 + c2 - 1)
    return max_len

def find_LDS_length_topdown(dp, nums, curr_idx, prev_idx):
    if curr_idx == len(nums):
        return 0
    c1 = 0
    if dp[curr_idx][prev_idx] == -1:
        if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
            c1 = 1 + find_LDS_length_topdown(dp, nums, curr_idx+1, curr_idx)
        c2 = find_LDS_length_topdown(dp, nums, curr_idx+1, prev_idx)
        dp[curr_idx][prev_idx] = max(c1, c2)
    return dp[curr_idx][prev_idx]

def find_LDS_length_topdown_rev(dp, nums, curr_idx, prev_idx):
    if curr_idx < 0:
        return 0
    c1 = 0
    if dp[curr_idx][prev_idx] == -1:
        if prev_idx == -1 or nums[curr_idx] < nums[prev_idx]:
            c1 = 1 + find_LDS_length_topdown_rev(dp, nums, curr_idx -1, curr_idx)
        c2 = find_LDS_length_topdown_rev(dp, nums, curr_idx -1, prev_idx)
        dp[curr_idx][prev_idx] = max(c1, c2)
    return dp[curr_idx][prev_idx]


def find_LBS_length_bottomup(nums):
    n = len(nums)
    lds = [0 for _ in range(n)]
    lds_rev = [0 for _ in range(n)]

    for i in range(n):
        lds[i] = 1
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], lds[j]+1)

    for i in range(n-1, -1, -1):
        lds_rev[i] = 1
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                lds_rev[i] = max(lds_rev[i], lds_rev[j] + 1)

    max_len = 0
    for i in range(n):
        max_len = max(max_len, lds[i]+lds_rev[i]-1)
    return max_len




print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))

print(find_LBS_length_topdown([4, 2, 3, 6, 10, 1, 12]))
print(find_LBS_length_topdown([4, 2, 5, 9, 7, 6, 10, 3, 1]))

print(find_LBS_length_bottomup([4, 2, 3, 6, 10, 1, 12]))
print(find_LBS_length_bottomup([4, 2, 5, 9, 7, 6, 10, 3, 1]))