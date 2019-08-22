"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        else:
            stack = []
            for i in range(len(s)):
                if not stack or s[i] == "{" or s[i] == "(" or s[i] == "{":
                    stack.append(s[i])
                else:
                    if (s[i] == "}" and stack[-1] == "{") or (s[i] == ")" and stack[-1] == "(") or (s[i] == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        stack.append(s[i])
        if stack:
            return False
        return True

if __name__ == "__main__":
    print Solution().isValid("()")
    print Solution().isValid("()[]{}")
    print Solution().isValid("(]")
    print Solution().isValid("([)]")
    print Solution().isValid("{[]}")
