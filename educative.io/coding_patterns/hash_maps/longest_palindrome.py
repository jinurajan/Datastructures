"""
Given a string, pal_string, consisting of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Note: Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

"""
from collections import Counter

from collections import Counter
def longest_palindrome(pal_string):
    char_counter = Counter(pal_string)
    exist_even, exist_odd = False, False
    length = 0
    for char in char_counter:
        if char_counter[char] % 2 == 0:
            length += char_counter[char]
            exist_even = True
        else:
            # odd number of occurences
            l = char_counter[char] // 2
            length += l * 2
            exist_odd = True
    if exist_odd:
        if length == 1:
            return 1
        return length + 1
    else:
        return length
