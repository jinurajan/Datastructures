"""
Valid Parentheses

Solution
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Time taken to solve: 33 mins including coding and testing
"""


class Stack():
    def __init__(self):
        self.ds = []

    def pop(self):
        return self.ds.pop()

    def add(self, val):
        self.ds.append(val)

    def top(self):
        return self.ds[-1]

    def is_empty(self):
        return True if not self.ds else False


class SolutionWithStack(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_map = {'{': '}', '[': ']', '(': ')'}
        if not s:
            return True
        elif len(s) % 2 != 0:
            return False
        elif len(s) == 2:
            return True if p_map.get(s[0]) == s[1] else False
        else:
            stack = Stack()
            i = 0
            while i < len(s):
                if stack.is_empty():
                    stack.add(s[i])
                elif p_map.get(stack.top()) == s[i]:
                    stack.pop()
                else:
                    stack.add(s[i])
                i = i + 1
            if stack.is_empty():
                return True
            return False


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        p_map = {'{': '}', '[': ']', '(': ')'}
        for i in s:
            if i in p_map:
                stack.append(i)
            else:
                if not stack or p_map[stack.pop()] != i: return False
        return len(stack) == 0



if __name__ == "__main__":
    # print Solution().isValid("()")
    print Solution().isValid("()[]{}")
    print Solution().isValid("(]")
    print Solution().isValid("([)]")
    print Solution().isValid("{[]}")
