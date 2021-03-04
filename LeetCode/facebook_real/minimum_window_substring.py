"""

minimum window substring

input = "abccd"

substring = abc

"""

from collections import Counter


class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window_chars = {}
        uniq = 0
        l, r = 0, 0
        min_len = float("inf")
        min_len_str = ""
        while r < len(s):
            char = s[r]
            window_chars[char] = window_chars.get(char, 0) + 1
            if char in counter and window_chars[char] == counter[char]:
                uniq += 1
            while l <= r and uniq == len(counter):
                char = s[l]
                if r - l +1 < min_len:
                    min_len = r -l +1
                    min_len_str = s[l:r+1]
                window_chars[char] -= 1
                if char in counter and window_chars[char] < counter[char]:
                    uniq -= 1
                l += 1
            r += 1
        return min_len_str



s = "ADOBECODEBANC"
t = "ABC"
print(Solution1().minWindow(s, t))

