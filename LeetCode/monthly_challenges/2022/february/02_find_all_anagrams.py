"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

"""
from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        output = []
        p_counter = Counter(p)
        s_counter = Counter(s)

        for i in range(ns):
            # add one more letter on the right
            s_counter[s[i]] += 1
            # remove one from left
            if  i >= np:
                # if count is 1 delete from dict
                if s_counter[s[i-np]] == 1:
                    del s_counter[s[i-np]]
                else:
                    s_counter[s[i-np]] -= 1
            # if both counters are equal
            if p_counter == s_counter:
                # add the start index to output
                output.append(i-np+1)
        return output


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        output = []
        p_counter = [0]*26
        s_counter = [0]*26
        for ch in p:
            p_counter[ord(ch) - ord('a')] += 1
        output = []
        for i in range(ns):
            s_counter[ord(s[i]) - ord('a')] += 1
            if i >= np:
                s_counter[ord(s[i-np]) - ord('a')] -= 1
        if p_counter == s_counter:
            output.append(i-np+1)
        return output



