"""
Longest Palindromic Substring

Given a string s, return the longest 
palindromic substring  in s.

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        result =[0, 0]
        for i in range(n):
            dp[i][i] = True
        for j in range(n-1):
            if s[j] == s[j+1]:
                dp[j][j+1] = True
                result = [j, j+1]
        
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    result = [i, j]
        i, j = result
        return s[i:j+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i,j):
            left = i
            right = j
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right-left - 1
        
        result = [0, 0]
        n = len(s)
        for i in range(n):
            odd_length = expand(i,i)
            if odd_length > result[1] - result[0]:
                dist = odd_length // 2
                result = [i-dist, i+dist]
            even_length = expand(i, i+1)
            if even_length > result[1] - result[0]:
                dist = (even_length // 2) - 1
                result = [i-dist, i+dist+1]
        i, j = result
        return s[i:j+1]
