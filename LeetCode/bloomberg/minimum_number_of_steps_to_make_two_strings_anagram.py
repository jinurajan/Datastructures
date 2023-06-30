"""
Minimum Number of Steps to Make Two Strings Anagram


You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.


Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        count = 0
        for char in t:
            if char in s_counter and s_counter[char]:
                s_counter[char] -= 1
            else:
                count += 1
        return sum(s_counter.values())


from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        total_count = 0
        for char, count in t_counter.items():
            if char in s_counter and count > s_counter[char]:
                total_count += abs(count-s_counter[char])
            elif char not in s_counter:
                total_count += count
        return total_count

