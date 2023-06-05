"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


"""

import math
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force
        m = len(s)
        min_len = math.inf
        min_len_str = ""
        t_counter = Counter(t)
        start = 0
        end = 0
        current_chars = 0
        required_chars = len(t_counter)
        window_counter = Counter()
        while end < m:
            print(start, end, window_counter, t_counter)
            import pdb; pdb.set_trace()
            if s[end] in t_counter:
                window_counter[s[end]] += 1
                if window_counter[s[end]] == t_counter[s[end]]:
                    current_chars += 1
                while start <=end and current_chars == required_chars:
                    if min_len > end - start + 1:
                        min_len = end- start + 1
                        min_len_str = s[start:end+1]
                    if s[start] in t_counter:
                        window_counter[s[start]] -= 1
                    if s[start] in t_counter and window_counter[s[start]] < t_counter[s[start]]:
                        current_chars -= 1
                    start += 1
            end += 1
        return min_len_str
              

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        # brute force
        m = len(s)
        n = len(t)
        t_counter = Counter(t)

        def contains(c1, c2):
            # c1 is s_counter
            for key, value in c2.items():
                if key not in c1 or c1[key] < value:
                    return False
            return True
        min_len = math.inf
        min_length_str = ""
        for i in range(m):
            for j in range(1, m+1):
                s_counter = Counter(s[i:j])
                if contains(s_counter, t_counter):
                    # contains
                    if min_len > j-i:
                        min_len = j-i
                        min_length_str = s[i:j]
        return min_length_str


print(Solution().minWindow("aa", "aa"))