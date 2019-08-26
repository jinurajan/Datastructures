"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        else:
            j = 0
            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    end -= 1
                    if start == end:
                        start += 1
                        end = len(s) - 1
                else:
                    if self.longestPalindromeUtil(s, start, end):
                        return s[start:end + 1]
                    else:
                        j += 1
                        start = j
                        end = len(s) - 1
        return s[0]

    def longestPalindromeUtil(self, s, start, end):
        if start > end:
            return True
        if s[start] == s[end]:
            return self.longestPalindromeUtil(s, start + 1, end - 1)
        else:
            return False


if __name__ == "__main__":
    # print Solution().longestPalindromeUtil("a", 0, 0)
    # print Solution().longestPalindromeUtil("ab", 0, 1)
    # print Solution().longestPalindromeUtil("aba", 0, 2)
    # print Solution().longestPalindromeUtil("ababa", 0, 4)
    print Solution().longestPalindrome("babad")
    print Solution().longestPalindrome("babab")
    print Solution().longestPalindrome("cbbd")
    print Solution().longestPalindrome("ac")
    print Solution().longestPalindrome("babadada")

