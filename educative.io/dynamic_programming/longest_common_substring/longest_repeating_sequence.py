"""
Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

Example 1:

Input: “t o m o r r o w”
Output: 2
Explanation: The longest repeating subsequence is “or” {tomorrow}.

Example 2:

Input: “a a b d b c e c”
Output: 3
Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

Example 3:

Input: “f m f f”
Output: 2
Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.
"""

def find_LRS_length(str):
    return find_LRS_length_recursive(str, 0, 0)

def find_LRS_length_recursive(str, i1, i2):
    if i1 == len(str) or i2 == len(str):
        return 0
    if i1 != i2 and str[i1] == str[i2]:
        return 1 + find_LRS_length_recursive(str, i1+1, i2+1)

    c1 = find_LRS_length_recursive(str, i1+1, i2)
    c2 = find_LRS_length_recursive(str, i1, i2+1)
    return max(c1, c2)

def find_LRS_length_topdown(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LRS_length_recursive_topdown(dp, str, 0, 0)

def find_LRS_length_recursive_topdown(dp, str, i1, i2):
    if i1 == len(str) or i2 == len(str):
        return 0
    if dp[i1][i2] == -1:
        if i1 != i2 and str[i1] == str[i2]:
            return 1 + find_LRS_length_recursive(str, i1 + 1, i2 + 1)

        c1 = find_LRS_length_recursive(str, i1 + 1, i2)
        c2 = find_LRS_length_recursive(str, i1, i2 + 1)
        dp[i1][i2] = max(c1, c2)
    return dp[i1][i2]

def find_LRS_length_bottomup(str):
    n = len(str)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    max_len = 0
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            if i1 != i2 and str[i1-1] == str[i2-1]:
                dp[i1][i2] = 1 + dp[i1-1][i2-1]
            else:
                dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
            max_len = max(max_len, dp[i1][i2])
    return max_len





print(find_LRS_length("tomorrow"))
print(find_LRS_length("aabdbcec"))
print(find_LRS_length("fmff"))


print(find_LRS_length_topdown("tomorrow"))
print(find_LRS_length_topdown("aabdbcec"))
print(find_LRS_length_topdown("fmff"))

print(find_LRS_length_bottomup("tomorrow"))
print(find_LRS_length_bottomup("aabdbcec"))
print(find_LRS_length_bottomup("fmff"))
