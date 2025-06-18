"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_dict = set(wordDict)
        n = len(s)

        @lru_cache(maxsize=None)
        def can_word_break(start):
            if start == n:
                return True
            
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and can_word_break(end):
                    return True
            return False
        
        return can_word_break(0)


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # using bfs
        word_dict = set(wordDict)
        n = len(s)
        max_word_len = max(len(v) for v in word_dict) + 1
        q = [0]
        visited = {0}
        while q:
            start = q.pop(0)
            for end in range(start+1, start+max_word_len):
                if s[start:end] in word_dict and end not in visited:
                    if end == n:
                        return True
                    visited.add(end)
                    q.append(end)
        return False        
        

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution1().wordBreak(s, wordDict=wordDict))