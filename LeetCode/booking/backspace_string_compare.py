"""
Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def find_word(word):
            stack = []
            for char in word:
                if char != "#":
                    stack.append(char)
                else:
                    # time to pop
                    if stack:
                        stack.pop()
            return stack

        return find_word(s) == find_word(t)