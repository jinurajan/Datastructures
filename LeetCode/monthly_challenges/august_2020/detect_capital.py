"""
Detect Capital

Solution
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.__is_small(word[0]):
            return self.check_is_valid(1, word, self.__is_small)
        else:
            return self.check_is_valid(1, word, self.__is_capital) or\
            self.check_is_valid(1, word, self.__is_small)
    
    def check_is_valid(self, s_index, word, fn):
        result = True
        while s_index < len(word):
            result = fn(word[s_index])
            if result is False:
                return False
            s_index += 1
        return result
    
    def __is_capital(self, w):
        if ord(w) >=65 and ord(w)<= 90:
            return True
        else:
            return False

    def __is_small(self, w):
        if ord(w) >=97 and ord(w)<= 122:
            return True
        else:
            return False
        
        