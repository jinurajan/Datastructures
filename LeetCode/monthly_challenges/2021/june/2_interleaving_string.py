"""
Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bruteforce
        def is_interleave_recursive(i1, i2, i3):
            s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
            if s1_len == i1 and s2_len == i2 and i3 == len(s3):
                return True
            if i3 == len(s3):
                return False
            b1, b2 = False, False
            if i1 < s1_len and s1[i1] == s3[i3]:
                b1 = is_interleave_recursive(i1 + 1, i2, i3 + 1)
            if i2 < s2_len and s2[i2] == s3[i3]:
                b2 = is_interleave_recursive(i1, i2 + 1, i3 + 1)
            return b1 or b2

        return is_interleave_recursive(0, 0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # topdown with dp
        dp = {}
        def is_interleave_recursive(i1, i2, i3):
            s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
            if s1_len == i1 and s2_len == i2 and i3 == len(s3):
                return True
            if i3 == len(s3):
                return False
            key = f"{i1}-{i2}-{i3}"
            if key not in dp:
                b1, b2 = False, False
                if i1 < s1_len and s1[i1] == s3[i3]:
                    b1 = is_interleave_recursive(i1 + 1, i2, i3 + 1)
                if i2 < s2_len and s2[i2] == s3[i3]:
                    b2 = is_interleave_recursive(i1, i2 + 1, i3 + 1)
                dp[key]  = b1 or b2
            return dp[key]

        return is_interleave_recursive(0, 0, 0)



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bottom up with dp
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        dp = [[False for _ in range(s2_len+1)] for _ in range(s1_len+1)]
        if s1_len + s2_len != s3_len:
            return False
        for i in range(s1_len+1):
            for j in range(s2_len+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    if i > 0 and s1[i-1] == s3[i+j-1]:
                        dp[i][j] |= dp[i-1][j]
                    if j > 0 and s2[j-1] == s3[i+j-1]:
                        dp[i][j] |= dp[i][j-1]

        return dp[s1_len][s2_len]




# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# print(Solution().isInterleave(s1, s2, s3))
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# print(Solution().isInterleave(s1, s2, s3))
s1= "a"
s2 = ""
s3 = "c"
print(Solution().isInterleave(s1, s2, s3))
s1 = "ab"
s2 = "bc"
s3 = "babc"
print(Solution().isInterleave(s1, s2, s3))
