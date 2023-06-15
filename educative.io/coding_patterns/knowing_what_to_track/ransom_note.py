"""
Given two strings, “ransom note” and “magazine”, check if the ransom note can be constructed using the letters from the magazine string. Return TRUE if a ransom note can be constructed. Otherwise, return FALSE.
"""

from collections import Counter
def can_construct(ransom_note, magazine):
    # Write your code here
    magazine_counter = Counter(magazine)

    for char in ransom_note:
        if char not in magazine_counter or magazine_counter[char] <= 0:
            return False
        magazine_counter[char] -= 1
    return True