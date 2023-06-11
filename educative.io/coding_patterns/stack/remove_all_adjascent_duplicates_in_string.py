"""
You are given a string consisting of lowercase English letters. Repeatedly remove adjacent duplicate letters, one pair at a time. Both members of a pair of adjacent duplicate letters need to be removed.
"""

def remove_duplicates(string):
    stack = []

    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)
