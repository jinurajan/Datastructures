"""
Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

"""
from typing import List

from math import floor
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        1. find the length of the str including a space after every word except the last
        2. find the number of lines required to accomodate by length/maxWidth
        3. iterate through the list and stop until the length is above (do not include if the len of word exceeds the length)
        """
        
        def get_words(i):
            current_line = []
            curr_len = 0
            while i < len(words) and curr_len + len(words[i]) <= maxWidth:
                current_line.append(words[i])
                curr_len += len(words[i]) + 1 # for space
                i += 1
            
            return current_line

        def create_line(line, i):
            # total spaces required per words
            base_length = -1
            for word in line:
                base_length += len(word)+ 1
            
            # extra spaces to occupy
            extra_spaces = maxWidth - base_length

            # if only 1 word in line or is the last word just add extra spaces
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " "* extra_spaces
            
            # words to add spaces except the last one
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "
            
            for j in range(word_count):
                line[j] += " " * spaces_per_word
            
            return " ".join(line)


        result = []
        i = 0
        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            result.append(create_line(current_line, i))

        return result
