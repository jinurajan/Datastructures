"""
Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

Example 1:

Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".
Example 2:

Input: = "cddpd"
Output: 7
Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".
Example 3:

Input: = "pqr"
Output: 3
Explanation: Here are the palindromic substrings,"p", "q", "r".

"""

def count_PS(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        dp[i][i] = 1
        count += 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                if end - start == 1 or dp[start+1][end-1] == True:
                    dp[start][end] = True
                    count += 1
    return count

print(count_PS("abdbca"))
print(count_PS("cddpd"))
print(count_PS("pqr"))
print(count_PS("qqq"))