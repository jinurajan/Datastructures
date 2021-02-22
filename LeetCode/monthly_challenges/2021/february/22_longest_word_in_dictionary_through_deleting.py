"""
Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000
"""
from typing import List
from functools import cmp_to_key

class Solution2:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=cmp_to_key(lambda x, y: ((x > y) - (x < y))  if len(x) == len(y) else len(y) - len(x)))
        def is_subsequence(word):
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)
        for word in d:
            if is_subsequence(word):
                    return word
        return ""

class Solution1:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x),x) )
        def is_subsequence(word):
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)
        for word in d:
            if is_subsequence(word):
                    return word
        return ""

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = ""
        for w in d:
            diff = len(w) - len(result)
            if diff >= 0:
                if diff > 0 or w < result:
                    try:
                        pos = -1
                        for c in w:
                            pos = s.index(c, pos + 1)
                        result = w
                    except ValueError:
                        pass
        return result

s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(Solution().findLongestWord(s, d))
s = "abpcplea"
d = ["a","b","c"]
print(Solution().findLongestWord(s, d))
s = "aewfafwafjlwajflwajflwafj"
d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
print(Solution().findLongestWord(s, d))
s = "bab"
d = ["ba","ab","a","b"]
print(Solution().findLongestWord(s, d))
