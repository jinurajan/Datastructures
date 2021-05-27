"""
Maximum Product of Word Lengths

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.



Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_number = lambda ch: ord(ch) - ord('a')
        n = len(words)
        masks = [0] * n
        lengths = [0] * n
        for i in range(n):
            bitmask = 0
            for char in words[i]:
                bitmask |= 1 << bit_number(char)
            masks[i] = bitmask
            lengths[i] = len(words[i])
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lengths[i] * lengths[j])
        return max_val





