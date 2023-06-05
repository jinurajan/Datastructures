"""
Given a string s, return the longest 
palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP programming
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        result = [0, 0]
        for i in range(n):
            # single length palindromes
            dp[i][i] = True
        for i in range(n-1):
            # palindromes with even/2 length
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                result = [i, i+1]
    
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
        # expand around center
        def expand(i, j):
            left = i
            right = j
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right-left-1
        result = [0,0]
        n = len(s)
        for i in range(n):
            odd_length = expand(i, i)
            if odd_length > result[1]-result[0]+1:
                dist = odd_length // 2
                result = [i-dist, i+dist]
            even_length = expand(i, i+1)
            if even_length > result[1]-result[0]+1:
                dist = (even_length // 2 ) - 1
                result = [i-dist, i+1+dist]
        i, j = result
        return s[i:j+1]
        
