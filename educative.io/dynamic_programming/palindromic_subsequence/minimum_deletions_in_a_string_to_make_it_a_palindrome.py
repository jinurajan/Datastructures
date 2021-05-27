"""
Given a string, find the minimum number of characters that we can remove to make it a palindrome.

Example 1:

Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Deleting "cp", we get a palindrome "ddd".


similar problem:
1. Minimum insertions in a string to make it a palindrome
2. Find if a string is K-Palindromic #


"""


def find_minimum_deletions(st):
    return len(st) - find_LPS_length(st)


def find_LPS_length(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    return dp[0][n-1]

print(find_minimum_deletions("abdbca"))
print(find_minimum_deletions("cddpd"))
print(find_minimum_deletions("pqr"))
