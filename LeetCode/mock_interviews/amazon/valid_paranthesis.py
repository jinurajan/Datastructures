"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = deque([])
        open_brackets = {'(', '[', '{'}
        close_brackets = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != close_brackets[char]:
                    return False
        return len(stack) == 0

