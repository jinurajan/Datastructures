"""
Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string. The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.
"""

def calculator(expression):
    number = 0
    # for positive numbers
    sign_value = 1
    result = 0
    stack = []
    for c in expression:
        if c.isdigit():
            number = number * 10 + int(c)
        if c in {'+', '-'}:
            # operator
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        elif c == '(':
            # start of an operation
            stack.append(result)
            stack.append(sign_value)
            result = 0
            sign_value = 1
        elif c == ')':
            # end of an operation
            result += sign_value * number
            pop_sign_value = stack.pop()
            result *= pop_sign_value

            second_value = stack.pop()
            result += second_value
            number = 0
    
    return result + number * sign_value
    
    return 0