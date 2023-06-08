"""
Palindromic Substrings


Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand around a number
        n = len(s)
        count = 0
        if not n:
            return n
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
            count += dp[i][i]
        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])
            count += dp[i][i+1]
        for sublen in range(3, n+1):
            for i in range(n):
                j = i + sublen-1
                if j >= n:
                    continue
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                count += dp[i][j]
        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def is_palindrome(s):
            return s == s[::-1]
        
        count = 0
        n = len(s)
        for l in range(n):
            for r in range(l, n):
                count += is_palindrome(s[l:r+1])
        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        
        while i < len(s):
            r = i
            l = i
            duplicates = 1
            # Move right pointer to the last duplicate of value, s[i]
            while r < len(s) - 1 and s[r] == s[r+1]:
                r += 1
                duplicates += 1
            
			# Arithmetic sum
			# NOTE: Explaination of this below
            count += duplicates*(duplicates + 1)//2
            
            # Set the next starting point
            i = r + 1 
            
            # Expand outwards to find longer palindrome
            while r < len(s) - 1 and l > 0 and s[r + 1] == s[l - 1]:
                r += 1
                l -= 1
                count += 1

        return count