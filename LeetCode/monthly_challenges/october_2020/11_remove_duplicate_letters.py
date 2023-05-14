"""
Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occ = {char: i for i, char in enumerate(str)}
        stack = ['*']
        visited = set()
        for i, char in enumerate(s):
            if symbol in visited:
                continue
            while char < stack[-1] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return "".join(stack)[1:]

from collections import Counter

class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        h = Counter(s)
        ans = ""
        for char in s:
            if char in ans:
                h[char] -= 1
                continue
            while len(ans) > 0 and h[ans[-1]] >= 1 and ord(char) < ord(ans[-1]):
                ans = ans[:-1]
            h[char] -= 1
            ans += char
        return ans
        
