"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.


"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ''
        counter = Counter(t)
        required = len(counter)
        l, r = 0, 0
        uniq = 0
        window_counts = {}
        ans = float('inf'), None, None
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in counter and window_counts[char] == counter[char]:
                uniq += 1
            while l <= r and uniq == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                window_counts[char] -= 1
                if char in counter and window_counts[char] < counter[char]:
                    uniq -= 1

                l += 1
            r += 1
        if ans[0] == float("inf"):
            return ""
        return s[ans[1]:ans[2] + 1]


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ''
        counter = Counter(t)
        required = len(counter)
        filtered_s = []
        for i, char in enumerate(s):
            if char in counter:
                filtered_s.append((i, char))
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == counter[char]:
                formed += 1
            while l <= r and formed == required:
                char = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = end - start + 1, start, end
                window_counts[char] -= 1
                if window_counts[char] < counter[char]:
                    formed -= 1
                l += 1
            r += 1
        return '' if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]





