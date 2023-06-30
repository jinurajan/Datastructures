"""
Decode String


Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.


"""


class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        num = 0
        import pdb; pdb.set_trace()
        for char in s:
            print(stack, char)
            if char.isnumeric():
                num = num*10 + int(char)
            elif char == '[':
                stack.append(result)
                stack.append(num)
                result = ""
                num = 0
            elif char == ']':
                count = stack.pop()
                prev = stack.pop()
                result = prev + count * result
            else:
                result += char
        return result


s = "3[a]2[bc]"
print(Solution().decodeString(s=s))
s = "2[abc]3[cd]ef"