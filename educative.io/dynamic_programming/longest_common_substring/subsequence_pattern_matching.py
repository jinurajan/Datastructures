"""
Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1: Input: string: “baxmx”, pattern: “ax”
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

"""
def find_SPM_count(str, pat):
    return find_SPM_count_recursive(str, pat, 0, 0, 0)

def find_SPM_count_recursive(str, pat, i1, i2, count):
    if i2 == len(pat):
        return 1
    if i1 == len(str):
        return 0
    c1 = 0
    if str[i1] == pat[i2]:
        c1 = find_SPM_count_recursive(str, pat, i1+1, i2+1, count+1)
    c2 = find_SPM_count_recursive(str, pat, i1+1, i2, count)
    return c1 + c2

def find_SPM_count_topdown(str, pat):
    n = len(str)
    m = len(pat)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    return find_SPM_count_recursive_topdown(dp, str, pat, 0, 0, 0)

def find_SPM_count_recursive_topdown(dp, str, pat, i1, i2, count):
    if i2 == len(pat):
        return 1
    if i1 == len(str):
        return 0
    if dp[i1][i2] == -1:
        c1 = 0
        if str[i1] == pat[i2]:
            c1 = find_SPM_count_recursive(str, pat, i1 + 1, i2 + 1, count + 1)
        c2 = find_SPM_count_recursive(str, pat, i1 + 1, i2, count)
        dp[i1][i2] = c1 + c2
    return dp[i1][i2]

def find_SPM_count_bottomup(str, pat):
    n = len(str)
    m = len(pat)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m + 1):
            if str[i-1] == pat[j-1]:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
    return dp[n][m]



print(find_SPM_count("baxmx", "ax"))
print(find_SPM_count("tomorrow", "tor"))

print(find_SPM_count_topdown("baxmx", "ax"))
print(find_SPM_count_topdown("tomorrow", "tor"))

print(find_SPM_count_bottomup("baxmx", "ax"))
print(find_SPM_count_bottomup("tomorrow", "tor"))