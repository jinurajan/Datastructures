"""
License Key Formatting

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

"""
import deque

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        formatted_words = deque([])
        words = s.split("-")
        combined_str = ""
        for word in words:
            combined_str += word.upper()
        len_str = len(combined_str)
        end = len_str
        start = len_str
        while start > 0:
            start -= 1
            if end - start == k:
                formatted_words.appendleft(combined_str[start:end])
                if start != 0:
                    formatted_words.appendleft("-")            
                end = start
                start = end
            if start == 0 and end-start < k:
                formatted_words.appendleft(combined_str[start:end])
        return "".join(formatted_words)