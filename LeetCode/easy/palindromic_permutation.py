"""
Palindrome Permutation
Given a string s, return true if a permutation of the string could form a palindrome.



Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
"""

from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd_num = 0
        for k, v in counter.items():
            if v % 2 == 1:
                odd_num += 1
        return odd_num <= 1



