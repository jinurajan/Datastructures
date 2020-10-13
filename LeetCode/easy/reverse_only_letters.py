"""
Reverse Only Letters

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
class Solution1:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S or len(S) == 1:
            return S
        S = list(S)
        left = 0
        right = len(S)-1
        while left <= right:
            if not self.valid_char(S[left]):
                left += 1
            elif not self.valid_char(S[right]):
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        S = "".join(S)
        return S

    def valid_char(self, char):
        if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (
            ord(char) >= ord('A') and ord(char) <= ord('Z')):
            return True
        return False


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S or len(S) == 1:
            return S
        stack = [char for char in S if char.isalpha()]
        result = ""
        for char in S:
            if char.isalpha():
                result += stack.pop()
            else:
                result += char
        return result


print(Solution().reverseOnlyLetters("ab-cd"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))

