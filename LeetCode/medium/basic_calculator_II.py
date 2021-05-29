"""
Basic Calculator II
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def calculate(self, s: str) -> int:
        inner, outer, result, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer

s = "3+2*2"
print(Solution().calculate(s))

s = " 3/2 "
print(Solution().calculate(s))

s = " 3+5 / 2 "
print(Solution().calculate(s))