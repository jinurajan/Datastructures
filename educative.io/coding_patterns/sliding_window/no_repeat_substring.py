"""
Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

from collections import Counter
def non_repeat_substring(str):
  n = len(str)
  left = 0
  right = 0
  char_set = Counter()
  max_len = float("-inf")
  while right < n:
    char_set[str[right]] += 1
    while char_set[str[right]] > 1:
      char_set[str[left]] -= 1
      if char_set[str[left]] == 0:
        del char_set[str[left]]
      left += 1
    if len(char_set) == right - left + 1:
      max_len = max(max_len, right-left+1)
    right += 1
  return max_len


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
