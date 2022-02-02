"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()

        result = 0
        left = 0
        max_count = 0
        
        for right, char_right in enumerate(s):
            counter[char_right] += 1
            max_count = max(max_count, counter[char_right])

            while ((right-left)+1) - max_count > k:
                counter[s[left]] -= 1
                left += 1
            result = max(result, (right-left+1))
        return result
