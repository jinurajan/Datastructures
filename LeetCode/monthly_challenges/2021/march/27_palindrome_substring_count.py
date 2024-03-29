"""
Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        def is_palindrome(s):
            return s == s[::-1]

        count = 0
        n = len(s)
        for l in range(n):
            for r in range(l, n):
                count += is_palindrome(s[l:r + 1])
        return count

print(Solution().countSubstrings("abcd"))
