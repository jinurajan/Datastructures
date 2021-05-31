"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


from collections import Counter
def length_of_longest_substring(str, k):
  n = len(str)
  left = 0
  right = 0
  max_repeating_count = 0
  counter = Counter()
  max_len = 0
  while right < n:
    counter[str[right]] += 1
    max_repeating_count = max(max_repeating_count, counter[str[right]])
    if right - left + 1 - max_repeating_count > k:
      counter[str[left]] -= 1
      if counter[str[left]] == 0:
        del counter[str[left]]
      left += 1
    max_len = max(max_len, right-left+1)
    right += 1

  return max_len
