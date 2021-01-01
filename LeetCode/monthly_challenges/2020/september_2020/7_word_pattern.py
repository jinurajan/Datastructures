"""
Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

Time Taken : 30 mins  + 6 mins
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patterns = []
        stack = []
        s = str.split(" ")
        if len(set(pattern[:])) != len(set(s)) or len(pattern) != len(s):
            return False

        for c in pattern:
            if stack and stack[-1] == c:
                patterns.append("pop")
                stack.pop(-1)
            else:
                patterns.append("insert")
                stack.append(c)
        while stack:
            patterns.append("insert")
            stack.pop(-1)
        print patterns
        i = 0
        stack2 = []
        for w in s:
            if patterns[i] == 'pop':
                # when both elements are same
                if stack2 and stack2[-1] == w:
                    stack2.pop(-1)
                else:
                    return False
            if patterns[i] == "insert":
                if stack2 and stack2[-1] == w:
                    return False
                stack2.append(w)
            i += 1
        if not stack2 or patterns:
            return True
        return False


class Solution1(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # use hash
        s = str.split(' ')
        if len(pattern) != len(s):
            return False
        d = {}

        for i in range(len(pattern)):
            if pattern[i] in d:
                if s[i] != d[pattern[i]]:
                    return False
            else:
                if s[i] in d.values():
                    return False
            d[pattern[i]] = s[i]
        return True



print Solution().wordPattern('abba', "dog cat cat dog") == True
print Solution().wordPattern('abba', "dog cat cat fish") == False
print Solution().wordPattern('aaaa', "dog cat cat dog") == False
print Solution().wordPattern('abba', "dog dog dog dog") == False
print Solution().wordPattern("abaaba", "dog cat fish fish cat dog") == False
print Solution().wordPattern("aaa", "aa aa aa aa") == False

print "***************"

print Solution1().wordPattern('abba', "dog cat cat dog") == True
print Solution1().wordPattern('abba', "dog cat cat fish") == False
print Solution1().wordPattern('aaaa', "dog cat cat dog") == False
print Solution1().wordPattern('abba', "dog dog dog dog") == False
print Solution1().wordPattern("abaaba", "dog cat fish fish cat dog") == False
print Solution1().wordPattern("aaa", "aa aa aa aa") == False



