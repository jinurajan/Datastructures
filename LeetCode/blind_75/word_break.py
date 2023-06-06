"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


thinking

1. start from the end, create segments and check if exists in the set if yes reset the end value and move start towards the 0 if start reaches 0 and s[start:end] is in dict return True else False
    1. create a set of worddict
    2. end = n-1, start = n-1 do start -= 1 until we find a word in set and reset end=start-1 and deduct. issues ? we are not checking same other possible values from the beginning

"""
from typing import List
from typing import FrozenSet
from functools import lru_cache
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute force (recursion and backtracking and memoization with lrucache)
        @lru_cache
        def wordbreakrecur(s:str, word_dict: FrozenSet[str], start:int):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and wordbreakrecur(s, word_dict, end):
                    return True
            return False
        return wordbreakrecur(s, frozenset(wordDict), 0)



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bfs
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

