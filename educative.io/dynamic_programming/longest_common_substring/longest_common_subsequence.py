"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


Input: s1 = "abdca"
       s2 = "cbda"
Output: 3
Explanation: The longest common subsequence is "bda".


Input: s1 = "passport"
       s2 = "ppsspt"
Output: 5
Explanation: The longest common subsequence is "psspt".
"""

def find_LCS_length(s1, s2):
    if not s1 or not s2:
        return 0
    return find_LCS_length_recursive(s1, s2, 0, 0)

def find_LCS_length_recursive(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if s1[i1] == s2[i2]:
        return 1 + find_LCS_length_recursive(s1, s2, i1+1, i2+1)
    c1 = find_LCS_length_recursive(s1, s2, i1+1, i2)
    c2 = find_LCS_length_recursive(s1, s2, i1, i2+1)
    return max(c1, c2)


def find_LCS_length_top_down(s1, s2):
    if not s1 or not s2:
        return 0
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]
    return find_LCS_length_top_down_recursive(dp, s1, s2, 0, 0)

def find_LCS_length_top_down_recursive(dp, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if dp[i1][i2] == -1:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + find_LCS_length_top_down_recursive(dp, s1, s2, i1+1, i2+1)
        else:
            c1 = find_LCS_length_top_down_recursive(dp, s1, s2, i1+1, i2)
            c2 = find_LCS_length_top_down_recursive(dp, s1, s2, i1, i2+1)
            dp[i1][i2] = max(c1, c2)
    return dp[i1][i2]


def find_LCS_length_bottom_up(s1, s2):
    if not s1 or not s2:
        return 0
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    max_len = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_len = max(max_len, dp[i][j])
    return max_len

def find_LCS_length_bottom_up_optimized(s1, s2):
    if not s1 or not s2:
        return 0
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(2)]
    max_len = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i%2][j] = 1 + dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = max(dp[(i-1)% 2][j], dp[i%2][j-1])
            max_len = max(max_len, dp[i%2][j])
    return max_len



def find_LCS_length_bottom_up_optimized_2(text1: str, text2: str) -> int:
    if not text1 or not text2:
        return 0

    if len(text2) < len(text1):
        text1, text2 = text2, text1
    n1 = len(text1)
    n2 = len(text2)
    previous = [0] * (n1 + 1)
    current = [0] * (n1 + 1)
    for col in reversed(range(n2)):
        for row in reversed(range(n1)):
            if text2[col] == text1[row]:
                current[row] = 1 + previous[row + 1]
            else:
                current[row] = max(previous[row], current[row + 1])
        previous, current = current, previous
    return previous[0]


print(find_LCS_length("abdca", "cbda"))
print(find_LCS_length("passport", "ppsspt"))

print(find_LCS_length_top_down("abdca", "cbda"))
print(find_LCS_length_top_down("passport", "ppsspt"))


print(find_LCS_length_bottom_up("abdca", "cbda"))
print(find_LCS_length_bottom_up("passport", "ppsspt"))

print(find_LCS_length_bottom_up_optimized_2("abdca", "cbda"))
print(find_LCS_length_bottom_up_optimized_2("passport", "ppsspt"))