"""
For a given string, find whether or not a permutation of this string is a palindrome. You should return TRUE if such a permutation is possible and FALSE if it isn’t possible.
"""



# Tip: You may use some of the code templates provided
# in the support files
from collections import Counter

def permute_palindrome(st):
  char_counter = Counter(st)
  odd_count = 0
  for key, count in char_counter.items():
    if count % 2 == 1:
      odd_count += 1
    
  return odd_count <= 1