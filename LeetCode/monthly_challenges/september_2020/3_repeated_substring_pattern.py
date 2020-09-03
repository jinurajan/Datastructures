"""
Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""


class Solution1(object):
     def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = s[0]
        for i in range(1,(len(s)//2)+1):
            if set(s.split(temp)) == {''}:
                return True
            temp += s[i]
        return False


class Solution(object):
    """
        replicate elements. remove first and last char and check if s is present.
        if there is repetition.
    """
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = s+s
        return s in new_str[1:-1]


print Solution().repeatedSubstringPattern("abab") == True
print Solution().repeatedSubstringPattern("abcabcabc") == True
print Solution().repeatedSubstringPattern("aba") == False
print Solution().repeatedSubstringPattern("a") == False
print Solution().repeatedSubstringPattern("ababba") == False
print Solution().repeatedSubstringPattern("aabaaba") == False

print "************** Solution ************"

print Solution1().repeatedSubstringPattern("abab") == True
print Solution1().repeatedSubstringPattern("abcabcabc") == True
print Solution1().repeatedSubstringPattern("aba") == False
print Solution1().repeatedSubstringPattern("a") == False
print Solution1().repeatedSubstringPattern("ababba") == False
print Solution1().repeatedSubstringPattern("aabaaba") == False
