"""
Smallest Window containing Substring (hard) #
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

"""
from collections import Counter

def find_substring(str1, pattern):
    n = len(str1)
    left = 0
    right = 0
    char_frequency = Counter(pattern)
    matched = 0
    min_len = n + 1
    start = 0
    while right < n:
        if str1[right] in char_frequency:
            char_frequency[str1[right]] -= 1
            if char_frequency[str1[right]] == 0:
                matched += 1
        while matched == len(pattern):
            if min_len > right - left + 1:
                min_len = min(min_len, right-left+1)
                start = left
            if str1[left] in char_frequency:
                if char_frequency[str1[left]] == 0:
                    matched -= 1
                char_frequency[str1[left]] += 1
            left += 1
        right += 1
    return "" if min_len > n  else str1[start:start+min_len]

def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc"))

main()

