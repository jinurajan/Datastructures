"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"


Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(s, left, right):
            L = left
            R = right
            while L >=0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = expand(s, i, i)
            l2 = expand(s, i, i+1)
            l = max(l1, l2)
            if l > end-start+1:
                start = i - (l-1) // 2
                end = i + l // 2
        return s[start:end+1]


s = "babad"

print(Solution().longestPalindrome(s))





