"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complimentary_chars = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char not in complimentary_chars:
                stack.append(char)
            else:
                # time to pop
                if stack:
                    if stack[-1] != complimentary_chars[char]:
                        return False
                    stack.pop(-1)
                else:
                    return False
                
        return len(stack) == 0