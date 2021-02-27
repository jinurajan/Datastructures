"""
Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign *= -1
        if divisor < 0:
            divisor = -divisor
            sign *= -1
        if divisor == 1:
            result = dividend
        else:
            result = 0
            while dividend > divisor:
                dividend -= divisor
                result += 1
        if sign > 0 and result > pow(2, 31)-1:
            return pow(2, 31) - 1
        if sign < 0 and result > pow(2, 31):
            return pow(2, 31) * sign
        return result * sign



# dividend = 10
# divisor = 3
# print(Solution().divide(dividend, divisor))
dividend = pow(2, 31) + 1
divisor = 1
print(Solution().divide(dividend, divisor))

dividend = - (pow(2, 31) + 1)
divisor = 1
print(Solution().divide(dividend, divisor))

