"""
Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
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


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_indices = set()
        stack = []
        for i, char in enumerate(s):
            if char == ')':
                if not stack:
                    remove_indices.add(i)
                while stack and stack[-1][0] != '(':
                    stack.pop()
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
            else:
                stack.append((char, i))
        while stack:
            char, idx = stack.pop()
            if char == '(':
                remove_indices.add(idx)
        return "".join([char for i, char in enumerate(s) if i not in remove_indices])




