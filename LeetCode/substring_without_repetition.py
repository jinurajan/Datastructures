"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # max_len = 0
        # char_set = set()
        # i = 0
        # while i < len(s):
        #     if s[i] in char_set:
        #         max_len = len(char_set) if len(char_set) > max_len else max_len
        #         char_set = set()
        #         char_set.add(s[i])
        #     else:
        #         char_set.add(s[i])
        #     i = i + 1

        # return max_len if len(char_set) < max_len else len(char_set)
        max_len = 0
        char_set = {}
        i = 0
        while i < len(s):
            if s[i] in char_set:
                max_len = len(char_set) if len(char_set) > max_len else max_len
                prev_start_index = char_set[s[i]]
                i = prev_start_index + 1
                char_set = {}
                char_set[s[i]] = i
            else:
                char_set[s[i]] = i
            i = i + 1
        return max_len if len(char_set) < max_len else len(char_set)


if __name__ == "__main__":
    input = " "
    print Solution().lengthOfLongestSubstring(input)
    input = "abcabcbb"
    print Solution().lengthOfLongestSubstring(input)
    input = "bbbbb"
    print Solution().lengthOfLongestSubstring(input)
    input = "pwwkew"
    print Solution().lengthOfLongestSubstring(input)
    input = "dvdf"
    print Solution().lengthOfLongestSubstring(input)
