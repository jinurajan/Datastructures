"""
Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        length = 0
        hash_set = {}
        exist_odd = False
        exist_even = False
        for w in s:
            if w not in hash_set:
                hash_set[w] = 1
            else:
                hash_set[w] += 1
        for w in hash_set:
            if hash_set[w] % 2 == 0:
                length += hash_set[w]
                exist_even = True
            else:
                # odd numbers
                l = hash_set[w] // 2
                length += l * 2
                exist_odd = True
        if exist_odd:
            if exist_even:
                return length + 1
            else:
                if length > 1:
                    return length + 1
                else:
                    return 1
        else:
            return length


print Solution().longestPalindrome("") == 0
print Solution().longestPalindrome("c") == 1
print Solution().longestPalindrome("ccc") == 3
print Solution().longestPalindrome("abc") == 1
print Solution().longestPalindrome("abcb") == 3
print Solution().longestPalindrome("abccccdd") == 7
