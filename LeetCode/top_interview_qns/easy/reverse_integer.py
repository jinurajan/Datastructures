"""
Reverse Integer

Solution
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
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
from math import pow
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        elif x < 0:
            flag = -1
        else:
            flag = 1
        x = x*flag
        no_of_10s = 0
        array = []
        while x > 0:
            array.append(x%10)
            no_of_10s +=1
            x = x / 10
        result = 0
        for i in array:
            result += i*int((pow(10, no_of_10s-1)))
            no_of_10s -=1
        if result > pow(2, 31):
            return 0
        return result*flag
        
            

        