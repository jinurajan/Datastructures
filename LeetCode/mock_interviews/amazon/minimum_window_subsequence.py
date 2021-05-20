"""
Minimum Window Subsequence

Given strings s1 and s2, find the minimum (contiguous) substring part of s1, so that s2 is a subsequence of part.

If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.


Note:

All the strings in the input will only contain lowercase letters.
The length of s1 will be in the range [1, 20000].
The length of s2 will be in the range [1, 100].
"""
from collections import defaultdict, deque

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        chpositions = defaultdict(deque)
        start = count = -1

        for i, ch in enumerate(T):
            chpositions[ch].appendleft(i)  # we'll be iterating from last to first

        startpositions = [-1] * len(T)
        for i, ch in enumerate(S):
            if ch not in chpositions: continue
            for pos in chpositions[ch]:
                if pos == 0: startpositions[0] = i
                else: startpositions[pos] = startpositions[pos-1]
                if pos == len(T) - 1 and (start == -1 or count > i - startpositions[-1] + 1):
                    start = startpositions[-1]
                    count = i - startpositions[-1] + 1

        if start < 0: return ''
        return S[start:start+count]


s1 = "abcdebdde"
s2 = "bde"
print(Solution().minWindow(s1, s2))