"""
Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1, num2 = list(num1), list(num2)
        carry = 0
        total = 0
        pos = 1
        while num1:
            if not num2:
                n2 = 0
            else:
                n2 = ord(num2.pop()) - ord('0')
            n1 = ord(num1.pop()) - ord('0')
            s = n1 + n2 + carry
            carry = 0
            if s > 10:
                s = s % 10
                carry = 1
            total += s * pos
            pos *= 10
        if carry:
            total += carry * pos
            pos *= 10
        return str(total)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


