"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10
            reversed_number = reversed_number + x % 10;
            x = x / 10
        return reversed_number


if __name__ == "__main__":
    input = 123
    print Solution().reverse(input)
    input = -123
    print Solution().reverse(input)
    input = 120
    print Solution().reverse(input)
