"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for i, word in enumerate(strs):
            anagram_map[''.join(sorted(word))].append(i)
        result = []
        for key, val in anagram_map.items():
            result.append([strs[x] for x in val])
        return result


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            anagram_map[''.join(sorted(word))].append(word)
        return anagram_map.values()

anagram_map = defaultdict(list)
preprocessed = False


def find_anagrams(anagram, text):
    global preprocessed, anagram_map
    if preprocessed:
        return anagram_map.get(''.join(sorted(anagram.lower())), [])
    else:
        for word in text.split(" "):
            anagram_map[''.join(sorted(word.lower()))].append(word)
        preprocessed = True
        return anagram_map.get(''.join(sorted(anagram.lower())), [])

text = "Steal the pears from tesla and spare the tales"
print(find_anagrams('steal', text))
print(find_anagrams('pears', text))
