"""
Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]


Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Input: num = "3456237490", target = 9191
Output: []
Constraints:

0 <= num.length <= 10
num only contain digits.
"""
import operator
from typing import List


class Solution1:
    def addOperators(self, num: str, target: int) -> List[str]:
        "This does not work with operator priorities since we calculate from left to right"
        op_map = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        def compute(combination, next_digits, comp_val, target):
            print(combination, next_digits, comp_val, target)
            if not next_digits:
                if comp_val == target:
                    output.append(combination)
                return
            else:
                for op, func in op_map.items():
                    comp_val = func(comp_val, int(next_digits[0]))
                    compute(combination+op+next_digits[0], next_digits[1:], comp_val, target)
        output = []
        import pdb; pdb.set_trace()
        compute(num[0], num[1:], int(num[0]), target)
        return output

class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        N = len(num)
        output = []
        def recurse(index, prev, current, value, string):
            if index == N:
                if value == target and current == 0:
                    output.append("".join(string[1:]))
                return
            current = current * 10 + int(num[index])
            str_op = str(current)
            if current > 0:
                recurse(index+1, prev, current, value, string)
            string.append('+')
            string.append(str_op)
            recurse(index+1, current, 0, value+current, string)
            string.pop()
            string.pop()
            if string:
                string.append('-')
                string.append(str_op)
                recurse(index+1, -current, 0, value-current, string)
                string.pop()
                string.pop()

                string.append('*')
                string.append(str_op)
                recurse(index + 1, current*prev, 0, value-prev+(current*prev), string)
                string.pop()
                string.pop()
        recurse(0, 0, 0, 0, [])
        return output


# num = "123"
# target = 6
# print(Solution().addOperators(num, target))

num = "232"
target = 8
import pdb; pdb.set_trace()
print(Solution().addOperators(num, target))

# num = "105"
# target = 5
# print(Solution().addOperators(num, target))
#
# num = "00"
# target = 0
# print(Solution().addOperators(num, target))
#
# num = "3456237490"
# target = 9191
# print(Solution().addOperators(num, target))

