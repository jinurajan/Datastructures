"""
Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.



Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        start = 0
        end = 0
        max_val = 1
        hash_map = {}
        while end < len(s):
            hash_map[s[end]] = end
            end += 1
            if len(hash_map) == k+1:
                idx = min(hash_map.values())
                del hash_map[s[idx]]
                start = idx + 1
            max_val = max(max_val, end-start)
        return max_val



s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))


s = "aa"
k = 1
print(Solution().lengthOfLongestSubstringKDistinct(s, k))

s ='a'
k = 0
print(Solution().lengthOfLongestSubstringKDistinct(s, k))

s = 'aba'
k = 1
print(Solution().lengthOfLongestSubstringKDistinct(s, k))

s = "bacc"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))
