"""
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "ddd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".
"""

def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st)-1)


def find_LPS_length_recursive(st, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if st[start] == st[end]:
        return 2 + find_LPS_length_recursive(st, start+1, end-1)
    c1 = find_LPS_length_recursive(st, start+1, end)
    c2 = find_LPS_length_recursive(st, start, end-1)
    return max(c1, c2)

def find_LPS_length_top_bottom(st):
    n = len(st)
    dp = [[-1 for i in range(n)] for j in range(n)]

    def find_LPS_length(st, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if dp[start][end] == -1:
            if st[start] == st[end]:
                dp[start][end] = 2 + find_LPS_length_recursive(st, start+1, end-1)
            else:
                c1 = find_LPS_length_recursive(st, start+1, end)
                c2 = find_LPS_length_recursive(st, start, end-1)
                dp[start][end] = max(c1, c2)
        return dp[start][end]

    return find_LPS_length(st, 0, n-1)

def find_LPS_length_bottom_up(st):
    n = len(st)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    return dp[0][n-1]




print(find_LPS_length("abdbca"))
print(find_LPS_length("cddpd"))
print(find_LPS_length("pqr"))

print(find_LPS_length_top_bottom("abdbca"))
print(find_LPS_length_top_bottom("cddpd"))
print(find_LPS_length_top_bottom("pqr"))


print(find_LPS_length_bottom_up("abdbca"))
print(find_LPS_length_bottom_up("cddpd"))
print(find_LPS_length_bottom_up("pqr"))
