"""
Base 7
Given an integer num, return a string of its base 7 representation.

Input: num = 100
Output: "202"

Input: num = -7
Output: "-10"
 
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans, n = '', abs(num)
        while n:
            n, mod = divmod(n, 7)
            ans += str(mod)
        if num < 0:
            ans += '-'
        return ans[::-1]