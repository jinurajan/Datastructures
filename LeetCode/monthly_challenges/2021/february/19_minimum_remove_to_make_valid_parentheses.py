"""
Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""
from collections import deque


class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        if not s:
            return  res
        stack = []
        index_to_remove = set()
        for i, c in enumerate(s):
            if c not in set({'(', ')'}):
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                index_to_remove.add(i)
            else:
                stack.pop()
        index_to_remove = index_to_remove.union(stack)
        for i, c in enumerate(s):
            if i not in index_to_remove:
                res += c
        return res

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        if not s:
            return  res
        def format_closing(string, open, close):
            sb = []
            bal = 0
            for c in string:
                if c == open:
                    bal += 1
                if c == close:
                    if bal == 0:
                        continue
                    bal -= 1
                sb.append(c)
            return ''.join(sb)
        s = format_closing(s, '(', ')')
        s = format_closing(s[::-1], ')', '(')
        return s[::-1]



s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))
s = "a)b(c)d"
print(Solution().minRemoveToMakeValid(s))
s = "))(("
print(Solution().minRemoveToMakeValid(s))
s = "(a(b(c)d)"
print(Solution().minRemoveToMakeValid(s))







