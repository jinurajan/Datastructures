"""
Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

"""
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)

        def is_valid(val):
            return not val.startswith('0') and int(val) <= 26 

        @lru_cache(maxsize=None)
        def backtrack(idx):
            if idx == n:
                return 1
            if idx == n+1:
                return 0
            c1, c2 = 0, 0
            if is_valid(s[idx]):
                c1 = backtrack(idx+1)
            if is_valid(s[idx:idx+2]):
                c2 = backtrack(idx+2)
            return c1 + c2
        
        return backtrack(0)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[-1] 

        
    