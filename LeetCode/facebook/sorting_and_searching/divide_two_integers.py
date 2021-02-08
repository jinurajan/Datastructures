"""
Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = - 2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2 raised to 31,  2 raised to 31 − 1]. For this problem, assume that your function returns 2 raised to 31 − 1 when the division result overflows.

"""
from math import exp, log, pow


class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if dividend < 0 or divisor < 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return sign * quotient

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        temp = 0
        for i in range(31, -1, -1):
            if temp + (divisor << i ) <= dividend:
                temp += divisor << i
                quotient |= 1 << i
        if sign * quotient > pow(2, 31) - 1:
            return int(pow(2, 31) - 1)
        elif sign * quotient < -1 * pow(2, 31):
            return  -1 * int(pow(2, 31))
        else:
            return sign * quotient

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if (dividend == 0):
            return 0

        if (divisor == 1):
            return sign * dividend

        quotient = int(exp(log(dividend) - log(divisor)))
        if sign * quotient > pow(2, 31) - 1:
            return int(pow(2, 31) - 1)
        elif sign * quotient < -1 * pow(2, 31):
            return -1 * int(pow(2, 31))
        else:
            return sign * quotient


print(Solution().divide(-1, -1))
print(Solution().divide(10, 3))
print(Solution().divide(7, 3))
print(Solution().divide(0, 1))
print(Solution().divide(1, 1))
print(Solution().divide(1, 2))
print(Solution().divide(7, -3))
print(Solution().divide(-2147483648, -1))
print(Solution().divide(2147483648, -1))