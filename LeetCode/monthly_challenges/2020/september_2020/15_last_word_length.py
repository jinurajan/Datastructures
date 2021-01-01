"""
Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        if not words:
            return 0
        last_word_len = 0
        current_word_len = len(words[0])
        for word in words:
            if not word:
                continue
            last_word_len = current_word_len
            current_word_len = len(word)

        if current_word_len > 0:
            last_word_len = current_word_len
        
        return last_word_len


class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        print words
        if len(words) != 0:
            return(len(words[-1]))
        else:
            return 0
        

print Solution().lengthOfLastWord("Hello world")

print Solution().lengthOfLastWord("   Hello   world  ")

print Solution().lengthOfLastWord("a")
print Solution().lengthOfLastWord("   a")



print Solution1().lengthOfLastWord("Hello world")

print Solution1().lengthOfLastWord("   Hello   world  ")

print Solution1().lengthOfLastWord("a")
print Solution1().lengthOfLastWord("   a")
