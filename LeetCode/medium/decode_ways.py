"""
91. Decode Ways

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

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

"""


from functools import lru_cache


class Solution:

    @lru_cache(maxsize=None)
    def recursive_with_memo(self, index, s) -> int:
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        ans = self.recursive_with_memo(index+1, s)
        if int(s[index:index+2]) <= 26:
            ans += self.recursive_with_memo(index+2, s)
        return ans

    def numDecodings(self, s: str) -> int:
        return self.recursive_with_memo(0, s)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        hash_set = set()
        n = len(s)
        def backtrack(index, subset):
            if index >= n:
                if tuple(subset) not in hash_set:
                    hash_set.add(tuple(subset))
                return
            f_val = int(s[index:index+1])
            if not f_val or f_val == 0:
                return
            subset.append(f_val)
            backtrack(index+1, subset)
            subset.pop()
            s_val = int(s[index:index+2])
            if not s_val or s_val == 0 or s_val > 26:
                return
            subset.append(f_val)
            backtrack(index+2, subset)
            subset.pop()
        
        backtrack(0,[])
        return len(hash_set)

input='11111111111111111111111111111111111111111111'
print(Solution().numDecodings(input))