"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_val = 0
        count = 0
        last_started = 0
        i = 0
        while i < len(s):
            if s[i] in visited:
                visited = set()
                max_val = max(count, max_val)
                count = 0
                i = last_started + 1
                last_started = i
            else:
                count += 1
                visited.add(s[i])
                i += 1

        return max(count, max_val)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0
        start = 0
        chars = dict()
        for idx, char in enumerate(s):
            if not char in chars:
                chars[char] = idx
            else:
                dup_idx = chars[char]
                if dup_idx < start:
                    chars[char] = idx
                else:
                    max_val = max(max_val, idx-start)
                    start = dup_idx + 1
                    chars[char] = idx
        return max(max_val, len(s)-start)

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "pwwkew"
import pdb; pdb.set_trace()
print(Solution().lengthOfLongestSubstring(s))
s = ""
print(Solution().lengthOfLongestSubstring(s))
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))



