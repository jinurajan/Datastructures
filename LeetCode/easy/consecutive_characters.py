"""
Consecutive Characters

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""

class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            return 1
        first = 0
        last = 0
        max_count = 0
        while last < n:
            if s[first] != s[last]:
                # we have jumped to new char
                max_count = max(max_count, last - first)
                first = last
                last = first
            else:
                last += 1
        if first < last:
            max_count = max(max_count, last-first)
        return max_count


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            return 1
        prev = None
        count = 0
        max_count = 0
        for char in s:
            if char == prev:
                count += 1
            else:
                prev = char
                count = 1
            max_count = max(max_count, count)
        return max_count


print(Solution().maxPower('leetcode'))
print(Solution().maxPower("abbcccddddeeeeedcba"))
print(Solution().maxPower("triplepillooooow"))
print(Solution().maxPower("hooraaaaaaaaaaay"))
print(Solution().maxPower("tourist"))
            