"""
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

"""
from collections import Counter

def find_string_anagrams(str1, pattern):
    n = len(str1)
    left = 0
    right = 0
    char_frequency = Counter(pattern)
    matched = 0
    result = []
    while right < n:
        if str1[right] in char_frequency:
            char_frequency[str1[right]] -= 1
            if char_frequency[str1[right]] == 0:
                matched += 1
        if matched == len(char_frequency):
            result.append(left)
        if right >= len(pattern) - 1:
            if str1[left] in char_frequency:
                if char_frequency[str1[left]] == 0:
                    matched -= 1
                char_frequency[str1[left]] += 1
            left += 1
        right += 1
    return result

def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()

