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
        
        
            
print(Solution().backspaceCompare("ab#c", "ad#c"))
print(Solution().backspaceCompare("ab##", "c#d#"))
print(Solution().backspaceCompare("a#c", "b"))