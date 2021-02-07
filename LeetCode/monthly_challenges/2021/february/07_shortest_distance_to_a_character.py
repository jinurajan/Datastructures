"""
Shortest Distance to a Character

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.
"""
from typing import List
import math


class Solution1:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx_set = set()
        result = []
        for idx, char in enumerate(s):
            if char == c:
                idx_set.add(idx)
                result.append(0)
            else:
                result.append(float('inf'))
        for idx in idx_set:
            start_val = 1
            start_idx = idx-1
            while start_idx >= 0 and s[start_idx] != 0:
                if result[start_idx] > start_val:
                    result[start_idx] = start_val
                start_val += 1
                start_idx -= 1
            start_idx = idx+1
            start_val = 1
            while start_idx <= len(result)-1 and s[start_idx] != 0:
                if result[start_idx] > start_val:
                    result[start_idx] = start_val
                start_val += 1
                start_idx += 1
        return  result


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [None] * len(s)
        prev = -math.inf
        for idx, char in enumerate(s):
            if char == c:
                prev = idx
                ans[idx] = 0
            else:
                ans[idx] = idx - prev
        prev = math.inf
        for idx in reversed(range(len(s))):
            char = s[idx]
            if char == c:
                prev = idx
                ans[idx] = 0
            else:
                ans[idx] = min(ans[idx], prev-idx)
        return ans




s = "loveleetcode"
c = "e"
print(Solution().shortestToChar(s, c) == [3,2,1,0,1,0,0,1,2,2,1,0])
s = "aaab"
c = "b"
print(Solution().shortestToChar(s, c) == [3,2,1,0])








