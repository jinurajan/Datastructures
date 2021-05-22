"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        left = 0
        right = 0
        char_map = {}
        while right < n:
            if s[right] in char_map:
                left = max(char_map[s[right]], left)
            max_len = max(max_len, right-left+1)
            char_map[s[right]] = right + 1
            right += 1
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        char_set = set()
        max_len = 0
        while right < len(s):
            while s[right] in char_set:
                max_len = max(max_len, len(char_set))
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            right += 1
        max_len = max(max_len, len(char_set))
        return max_len