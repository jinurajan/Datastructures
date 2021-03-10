"""
Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1, stack2 = [], []

        def populate_stack(string, stack):
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        populate_stack(S, stack1)
        populate_stack(T, stack2)
        return stack1 == stack2


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []
        S = list(S)
        T = list(T)
        max_len = max(len(S), len(T))
        start = 0
        while start < max_len:
            char1 = S.pop(0) if S else None
            char2 = T.pop(0) if T else None
            if char1 == "#":
                if s1:
                    s1.pop()
            elif char1 is not None:
                s1.append(char1)
            if char2 == '#':
                if s2:
                    s2.pop()
            elif char2 is not None:
                s2.append(char2)
            start += 1
        return s1 == s2

