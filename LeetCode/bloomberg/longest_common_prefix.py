"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force
        if not strs:
            return ""
        min_length = len(strs[0])
        for i in range(1, len(strs)):
            min_length = min(min_length, len(strs[i]))
        result = ""
        for i in range(min_length):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != current:
                    return result
            result += current
        return result


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the array alphabetically and compare the first nd last words only
        if not strs:
            return ""
        result = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use zip to get chars from each words and len(set(each chars) == 1 if they are same else return
        result = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                result += char[0]
            else:
                return result
        return result
