"""
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


from collections import Counter
def find_permutation(str, pattern):
  n = len(str)
  left = 0
  right = 0
  k = len(pattern)
  char_count = Counter(pattern)
  window_count = Counter()

  def is_equal(counter_1, counter_2):
    return counter_1 == counter_2

  while right < n:
    window_count[str[right]] += 1
    if right - left + 1 == k:
      if is_equal(window_count, char_count):
        return True
      window_count[str[left]] -= 1
      if window_count[str[left]] == 0:
        del window_count[str[left]]
      left += 1
    right += 1
  return False
