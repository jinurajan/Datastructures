"""
Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        bal_factor = 0
        ans = 0
        for idx, n in enumerate(S):
            if n == "(":
                bal_factor += 1
            else:
                bal_factor -= 1
                if S[idx - 1] == '(':
                    ans += 1 << bal_factor
        return ans
