"""
Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        word_dict = set(wordDict)
        cache = {}
        def breaker(s):
            if s not in cache:
                for w in word_dict:
                    if s[:len(w)] == w:
                        if len(s) == len(w):
                            cache[s] = True
                            return True
                        cache[s] = breaker(s[len(w):])
                        if cache[s]:
                            return True
                cache[s] = False
            return cache[s]
        return breaker(s)

from collections import deque

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        import pdb; pdb.set_trace()
        word_dict = set(wordDict)
        max_w = max(len(w) for w in word_dict) + 1
        dq = deque([0])
        visited = set([0])
        while dq:
            start = dq.popleft()
            for end in range(start, start+max_w):
                w = s[start:end]
                if w in word_dict and end not in visited:
                    if end == len(s):
                        return True
                    dq.append(end)
                    visited.add(end)
        return False




# print Solution().wordBreak("leetcode", wordDict = ["leet", "code"])
print Solution().wordBreak("applepenapple", wordDict = ["apple", "pen"])
# print Solution().wordBreak("catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
# print Solution().wordBreak("aaaaaaa",["aaaa","aaa"])
