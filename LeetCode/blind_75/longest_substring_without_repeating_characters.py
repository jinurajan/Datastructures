"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        end = 0
        char_map = {}
        n = len(s)
        for end in range(n):
            if s[end] in char_map:
                start = max(char_map[s[end]], start)
            max_len = max(max_len, end-start+1)
            char_map[s[end]] = end+1
        return max_len
