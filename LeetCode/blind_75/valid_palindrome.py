"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        first = 0
        last = len(s)-1
        while first <= last:
            if not s[first].isalnum():
                first += 1
                continue
            if not s[last].isalnum():
                last -= 1
                continue
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
        
        left = 0 
        right = len(result)-1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True

