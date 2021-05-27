"""
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

Example 1:

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Palindrome pieces are "c", "d", "dpd".
"""

def find_MPP_cuts(st):
    return find_MPP_cuts_recursive(st, 0, len(st)-1)

def is_palindrome(st, start, end):
    while start < end:
        if st[start] != st[end]:
            return False
        start += 1
        end -= 1
    return True

def find_MPP_cuts_recursive(st, start, end):
    if start >= end or is_palindrome(st, start, end):
        return 0
    min_cuts = end - start
    for i in range(start, end+1):
        if is_palindrome(st, start, i):
            min_cuts = min(min_cuts, 1+ find_MPP_cuts_recursive(st, i+1, end))
    return min_cuts


def find_MPP_cuts_top_down(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp_palindrome = [[-1 for _ in range(n)] for _ in range(n)]
    return find_MPP_cuts_recursive_top_down(dp, dp_palindrome, st, 0, n-1)

def find_MPP_cuts_recursive_top_down(dp, dp_palindrome, st, start, end):
    if start >= end or is_palindrome_topdown(dp_palindrome, st, start, end):
        return 0
    if dp[start][end] == -1:
        min_cuts = end - start
        for i in range(start, end+1):
            if is_palindrome(st, start, i):
                min_cuts = min(min_cuts, 1+ find_MPP_cuts_recursive_top_down(dp, dp_palindrome, st, i+1,end))
        dp[start][end] = min_cuts
    return dp[start][end]

def is_palindrome_topdown(dpIsPalindrome, st, x, y):
  if dpIsPalindrome[x][y] == -1:
    dpIsPalindrome[x][y] = 1
    i, j = x, y
    while i < j:
      if st[i] != st[j]:
        dpIsPalindrome[x][y] = 0
        break
      i += 1
      j -= 1
      # use memoization to find if the remaining string is a palindrome
      if i < j and dpIsPalindrome[i][j] != -1:
        dpIsPalindrome[x][y] = dpIsPalindrome[i][j]
        break
  return True if dpIsPalindrome[x][y] == 1 else False


def find_MPP_cuts_bottomup(st):
    n = len(st)
    is_palindrome = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                if end - start == 1 or is_palindrome[start+1][end-1]:
                    is_palindrome[start][end] = True
    cuts = [0 for _ in range(n)]
    for start in range(n-1, -1, -1):
        min_cuts = n
        for end in range(n-1, start-1, -1):
            if is_palindrome[start][end]:
                min_cuts = 0 if end == n-1 else min(min_cuts, 1+cuts[end+1])
        cuts[start] = min_cuts
    return cuts[0]


print(find_MPP_cuts("abdbca"))
print(find_MPP_cuts("cdpdd"))
print(find_MPP_cuts("pqr"))
print(find_MPP_cuts("pp"))
print(find_MPP_cuts("madam"))


print(find_MPP_cuts_top_down("abdbca"))
print(find_MPP_cuts_top_down("cdpdd"))
print(find_MPP_cuts_top_down("pqr"))
print(find_MPP_cuts_top_down("pp"))
print(find_MPP_cuts_top_down("madam"))


print(find_MPP_cuts_bottomup("abdbca"))
print(find_MPP_cuts_bottomup("cdpdd"))
print(find_MPP_cuts_bottomup("pqr"))
print(find_MPP_cuts_bottomup("pp"))
print(find_MPP_cuts_bottomup("madam"))
