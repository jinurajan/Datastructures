"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""
from bisect import bisect_right
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_idx_map = defaultdict(list)
        for idx, char in enumerate(t):
            char_idx_map[char].append(idx)
        curr_match_index = -1
        for char in s:
            if char not in char_idx_map:
                return False
            indices = char_idx_map[char]
            match_idx = bisect_right(indices, curr_match_index)
            if match_idx != len(indices):
                curr_match_index = indices[match_idx]
            else:
                return False
        return True   

class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        left, right = 0, 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)
            



class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def is_subseq(left, right):
            if left == len(s):
                return True
            if right == len(t):
                return False
            if s[left] == t[right]:
                left += 1
            right += 1
            return is_subseq(left, right)
        return is_subseq(0, 0)
