"""
First Unique Character in a String

Solution
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
"""

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
            