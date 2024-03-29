"""
Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
Constraints:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.

"""
from functools import lru_cache

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        @lru_cache(None)
        def reduce(source, target):
            if not source: return target
            if not target: return source
            if len(source) >= len(target):
                source, target = target, source
            if target[:len(source)] == source:
                return reduce(target[len(source):], source)
            return ""
        return reduce(str1, str2)



from math import gcd
class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[: gcd(len(str1), len(str2))]
        else:
            return ''

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1: return str2
        if not str2: return str1
        str1, str2 = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
        if str2[:len(str1)] == str1:
            return self.gcdOfStrings(str2[len(str1):], str1)
        return ''

str1 = "ABCABC"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2))