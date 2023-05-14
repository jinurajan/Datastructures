"""
Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

from math import log, ceil, floor


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        log_4 = log(num, 4)
        if floor(log_4) == ceil(log_4):
            return True
        return False

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        

if __name__ == "__main__":
	print Solution().isPowerOfFour(14)
	print Solution().isPowerOfFour(16)
	print Solution().isPowerOfFour(-4)
	print Solution().isPowerOfFour(-2147483648)