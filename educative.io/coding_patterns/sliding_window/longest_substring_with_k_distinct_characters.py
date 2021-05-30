"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

"""

from collections import Counter
def longest_substring_with_k_distinct(str, k):
  n = len(str)
  left = 0
  right = 0
  char_map = Counter()
  max_len = float("-inf")
  while right < n:
    char_map[str[right]] += 1
    if len(char_map) == k:
      max_len = max(max_len, right - left + 1)
    while len(char_map) > k:
      char_map[str[left]] -= 1
      if char_map[str[left]] == 0:
        del char_map[str[left]]
      left += 1
    right += 1
  return max_len


