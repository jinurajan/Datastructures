"""
First Unique Character in a String

Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ordered_dict = OrderedDict()
        for i, char in enumerate(s):
            if char in ordered_dict:
                ordered_dict[char].append(i)
            else:
                ordered_dict[char] = [i]
        for key, val in ordered_dict.items():
            if len(val) == 1:
                return val[0]
        return -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        elif len(s) == 1:
            return 0
        else:
            hash_set = {}
            for i in range(len(s)):
                if s[i] not in hash_set:
                    hash_set[s[i]] = [i, 1]
                else:
                    hash_set[s[i]][1] +=1
            uniq_index = -1
            for key, val in hash_set.items():
                if val[1] == 1:
                    if uniq_index == -1:
                        uniq_index = val[0]
                    if val[0] < uniq_index:
                        uniq_index = val[0]
            return uniq_index