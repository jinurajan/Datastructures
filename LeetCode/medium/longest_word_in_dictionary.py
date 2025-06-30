"""
720. Longest Word in Dictionary

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.

"""
from typing import List
from collections import defaultdict
from functools import reduce

class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans

class Solution1:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        # start with chars in the first node
        stack = list(trie.values()) 
        result = ""
        while stack:
            curr = stack.pop()
            if END in curr:
                word = words[curr[END]]
                if len(word) > len(result) or (len(word) == len(result) and word < result): 
                    result = word
                stack.extend([curr[letter] for letter in curr if letter!=END])
        return result

if __name__ == "__main__":
    words = ["w","wo","wor","worl","world"]
    print(Solution().longestWord(words=words))
    print(Solution1().longestWord(words=words))