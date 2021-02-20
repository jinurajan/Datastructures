"""
 Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""
from collections import deque


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = deque([-1])
        max_val = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_val = max(max_val, i - stack[-1])
        return max_val

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = deque([-1])
        import pdb; pdb.set_trace()
        max_val = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_val = max(max_val, i - stack[-1])
        return max_val


s = "()(()"
print(Solution().longestValidParentheses(s))
s = ")()())"
print(Solution().longestValidParentheses(s))



