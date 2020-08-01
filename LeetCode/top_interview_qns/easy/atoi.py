"""
String to Integer (atoi)
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range:
If the numerical value is out of the range of representable values, INT_MAX  or INT_MIN is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN is returned.
"""
from math import pow


def is_invalid_char(val):
    if val == ' ':
        return True
    val = ord(val)
    if (val >= 65 and val <= 90) or (val >= 97 and val <= 122) or val == '.':
        return True
    return False


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        left = 0
        right = len(s) - 1
        while s[left] == ' ':
            left += 1
        if is_invalid_char(s[left]):
            return 0
        while left < right:
            invalid_left = is_invalid_char(s[left])
            invalid_right = is_invalid_char(s[right])
            if invalid_left:
                left += 1
            if invalid_right:
                right -= 1
            if not invalid_left and not invalid_right:
                break
        flag = 1
        no_of_base_10 = right - left
        if s[left] == '-':
            flag = -1
            no_of_base_10 -= 1
            left += 1
        result = 0
        while left <= right:
            result += int((ord(s[left]) - ord('0')) * pow(10, no_of_base_10))
            no_of_base_10 -= 1
            left += 1
        result = flag * result
        if flag == -1 and result < -pow(2, 31):
            # check if - 2 raised to 31
            return -int(pow(2, 31))
        elif flag == 1 and result > pow(2, 31):
            return int(pow(2, 31)) - 1
        return int(result)

if __name__ == "__main__":
    print Solution().myAtoi("42")
    print Solution().myAtoi("   -42")
    print Solution().myAtoi("4193 with words")
    print Solution().myAtoi("words and 987")
    print Solution().myAtoi("-91283472332")
    print Solution().myAtoi("3.14159")
