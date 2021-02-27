"""
Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        import pdb; pdb.set_trace()
        sign = '+'
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            sign = '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res, rem = divmod(numerator, denominator)
        res = str(res) if sign == '+' else f'-{res}'
        if not rem:
            return res
        res += '.'
        d = {}
        while rem:
            if rem in d:
                res = f"{res[:d[rem]]}({res[d[rem]:]})"
                break
            d[rem] = len(res)
            rem *= 10
            res += str(rem // denominator)
            rem %= denominator
        return res


numerator = 1
denominator = 2
print(Solution().fractionToDecimal(numerator, denominator))

numerator = 4
denominator = 333
print(Solution().fractionToDecimal(numerator, denominator))