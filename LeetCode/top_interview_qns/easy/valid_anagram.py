"""
Valid Anagram

Solution
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


class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        elif len(s) == 1:
            return s == t
        hash_list = [0]*26
        for i in s:
            hash_list[ord(i) % 26] +=1
        for j in t:
            val = ord(j) % 26
            hash_list[val] -= 1
            if hash_list[val] < 0:
                return False
        return sum(hash_list) == 0


class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        elif len(s) == 1:
            return s == t
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 0
            hash_map[i] = hash_map[i] + 1
        for j in t:
            if j not in hash_map:
                return False
            if hash_map[j] < 0:
                return False
            hash_map[j] = hash_map[j]-1
        for key, val in hash_map.items():
            if val > 0:
                return False
        return True