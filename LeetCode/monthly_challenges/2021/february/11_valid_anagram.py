"""
Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import Counter


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = Counter(s)
        for char in t:
            try:
                char_map[char] -= 1
                if not char_map[char]:
                    del char_map[char]
            except KeyError:
                return False
        if char_map:
            return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_t = Counter(s)
        counter_s = Counter(t)
        return counter_t == counter_s

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))


s = "rat"
t = "car"
print(Solution().isAnagram(s, t))

