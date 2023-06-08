"""
Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations

"""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        start = 0
        frequency_map = Counter()
        max_frequency = 0
        long_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] += 1
            max_frequency = max(max_frequency, frequency_map[s[end]])

            is_valid = (end-start+1 - max_frequency) <= k
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1
            long_length = max(long_length, end-start+1)
        
        return long_length