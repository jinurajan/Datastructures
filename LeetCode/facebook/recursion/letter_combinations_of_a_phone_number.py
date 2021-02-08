"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9']
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def backtrack(combination, next_digit):
            print(combination, next_digit)
            if not next_digit:
                output.append(combination)
            else:
                for letter in char_map[next_digit[0]]:
                    backtrack(combination + letter, next_digit[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output

class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        sol = self.letterCombinations(digits[1:])
        if not sol:
            sol = [""]
        final_sol = []
        for first in char_map[digits[0]]:
            for last in sol:
                final_sol.append(first + last)
        return final_sol

digits = "23"
import pdb; pdb.set_trace()
print(Solution().letterCombinations(digits))

# digits = "2"
# print(Solution().letterCombinations(digits))
#
# digits = ""
# print(Solution().letterCombinations(digits))
