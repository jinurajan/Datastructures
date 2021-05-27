"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".
"""


def find_LCS_length(s1, s2):
    if not s2 or not s1:
        return ""
    return find_LCS_length_recursive(s1, s2, 0, 0, 0)


def find_LCS_length_recursive(s1, s2, index1, index2, count):
    if index1 == len(s1) or index2 == len(s2):
        return count
    if s1[index1] == s2[index2]:
        count= find_LCS_length_recursive(s1, s2, index1+1, index2+1, count+1)

    c1 = find_LCS_length_recursive(s1, s2, index1, index2+1, 0)
    c2 = find_LCS_length_recursive(s1, s2, index1+1, index2, 0)
    return max(count, max(c1, c2))


def find_LCS_length_top_down(s1, s2):
    if not s2 or not s1:
        return ""
    n = len(s1)
    m = len(s2)
    max_len = min(n, m)
    dp = [[[-1 for _ in range(max_len)] for _ in range(m)] for _ in range(n)]
    return  find_LCS_length_top_down_recursive(dp, s1, s2, 0, 0, 0)


def find_LCS_length_top_down_recursive(dp, s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count
    if dp[i1][i2][count] == -1:
        c1 = count
        if s1[i1] == s2[i2]:
            c1 = find_LCS_length_top_down_recursive(dp, s1, s2, i1+1, i2+1, count+1)
        c2 = find_LCS_length_top_down_recursive(dp, s1, s2, i1+1, i2, 0)
        c3 = find_LCS_length_top_down_recursive(dp, s1, s2, i1, i2+1, 0)
        dp[i1][i2][count] = max(c1, max(c2,c3))
    return dp[i1][i2][count]


def find_LCS_length_bottom_up(s1, s2):
    if not s2 or not s1:
        return ""
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_len = max(max_len, dp[i][j])
    return max_len

def find_LCS_length_bottom_up_optimized(s1, s2):
    if not s2 or not s1:
        return ""
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(2)]
    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i % 2][j] = 0
            if s1[i-1] == s2[j-1]:
                dp[i % 2][j] = 1 + dp[(i-1) % 2][j-1]
                max_len = max(max_len, dp[i%2][j])
    return max_len



print(find_LCS_length("abdca", "cbda"))
print(find_LCS_length("passport", "ppsspt"))

print(find_LCS_length_top_down("abdca", "cbda"))
print(find_LCS_length_top_down("passport", "ppsspt"))

print(find_LCS_length_bottom_up("abdca", "cbda"))
print(find_LCS_length_bottom_up("passport", "ppsspt"))

print(find_LCS_length_bottom_up_optimized("abdca", "cbda"))
print(find_LCS_length_bottom_up_optimized("passport", "ppsspt"))