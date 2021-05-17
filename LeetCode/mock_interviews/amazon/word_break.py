"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        word_dict = set(wordDict)
        max_word_len = max(len(v) for v in word_dict) + 1
        q = [0]
        seen = {0}
        while q:
            start = q.pop(0)
            for end in range(start, start + max_word_len):
                w = s[start:end]
                if w in word_dict and end not in seen:
                    if end == len(s):
                        return True
                    q.append(end)
                    seen.add(end)
        return False


s = "leetcode"
wordDict = ["leet","code"]
print(Solution().wordBreak(s, wordDict))
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s, wordDict))

