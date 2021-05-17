"""
Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def takeAWord(st):
            poss = [w for w in wordDict if st.startswith(w)]
            for p in poss:
                yield [p, st[len(p):]]

        q = [x for x in list(takeAWord(s))]
        ret = []

        while q:
            attempt = q.pop()
            if len(attempt[1]) > 0:
                more_attempts = [[attempt[0] + ' ' + x[0], x[1]] for x in list(takeAWord(attempt[1]))]
                q.extend(more_attempts)
            else:
                ret.append(attempt[0])
        return ret

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))