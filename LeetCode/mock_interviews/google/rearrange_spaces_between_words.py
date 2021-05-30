"""
Rearrange Spaces Between Words
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return "".join(words) + ' ' * spaces
        spaces, rem = divmod(spaces, len(words) - 1)
        return (" " * spaces).join(words) + " " * rem


class Solution:
    def reorderSpaces(self, text: str) -> str:
        no_of_spaces = 0
        words = text.split(" ")
        words = [w for w in words if w != '']
        for char in text:
            if char == " ":
                no_of_spaces += 1
        if len(words) == 1:
            result = "".join(words)
            result += " " * no_of_spaces
        else:
            spaces, rem = divmod(no_of_spaces, (len(words) - 1))
            space = " " * spaces
            result = space.join(words)
            if rem:
                result += " " * rem

        return result

