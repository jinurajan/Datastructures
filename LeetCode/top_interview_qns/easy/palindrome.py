"""
Valid Palindrome

Solution
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""


def is_special_char(val):
    try:
        int(val)
        return False
    except ValueError:
        val = ord(val)
        if (val >=65 and val <=90) or (val >=97 and val <= 122):
            return False
        return True


class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        int value range for small case - 
        """
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if is_special_char(s[left]):
                left += 1
            elif is_special_char(s[right]):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

char_set = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        int value range for small case
        """
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] not in char_set:
                left += 1
            elif s[right] not in char_set:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

if __name__ == "__main__":
    print Solution().isPalindrome("0P")
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
    print Solution().isPalindrome("race a car")
