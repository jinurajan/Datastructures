"""
Given a string, s, that may have matched and unmatched parentheses, remove the minimum number of parentheses so that the resulting string represents a valid parenthesization. For example, the string “a(b)” represents a valid parenthesization while the string “a(b” doesn’t, since the opening parenthesis doesn’t have any corresponding closing parenthesis.

"""

def min_remove_parentheses(s):
    stack = []

    for idx, char in enumerate(s):
        if stack and stack[-1][0] == '(' and char == ')':
            stack.pop()
        elif char == '(' or char == ')':
            stack.append([char, idx])
    
    result = []
    for i, char in enumerate(s):
        if [char, i] not in stack:
            result.append(s[i])
    
    return "".join(result)