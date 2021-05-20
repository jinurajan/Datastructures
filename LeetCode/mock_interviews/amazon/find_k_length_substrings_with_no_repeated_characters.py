"""
Find K-Length Substrings With No Repeated Characters
Given a string s, return the number of substrings of length k with no repeated characters.



Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation:
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation:
Notice k can be larger than the length of s. In this case is not possible to find any substring.


Note:

1 <= s.length <= 104
All characters of s are lowercase English letters.
1 <= k <= 104
"""


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0
        left = 0
        right = 0
        n = len(s)
        char_set = Counter()
        count = 0
        while right < n:
            char_set[s[right]] += 1
            if right - left + 1 == k:
                # consecutive k chars
                if len(char_set) == k:
                    # k unique chars
                    count += 1
                char_set[s[left]] -= 1
                if char_set[s[left]] == 0:
                    del char_set[s[left]]
                left += 1
            right += 1

        return count




