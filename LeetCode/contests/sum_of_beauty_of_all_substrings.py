"""
Sum of Beauty of All Substrings

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17

"""
class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                result += max(freq) - min(x for x in freq if x)
        return result


