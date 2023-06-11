"""
Given a string that may consist of opening and closing parentheses, your task is to check if the string contains valid parenthesization or not.

The conditions to validate are:

Every opening parenthesis should be closed by the same kind of parenthesis. So, {)and [(]) strings are invalid.

Every opening parenthesis must be closed in the correct order. So, )( and ()(() are invalid.

"""


def is_valid(string):
    stack = []
    compliments = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char not in compliments:
            stack.append(char)
        else:
            if stack and stack[-1] == compliments[char]:
                stack.pop()
            else:
                return False
            
    return not stack