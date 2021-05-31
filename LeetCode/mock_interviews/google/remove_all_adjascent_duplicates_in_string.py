"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

"""

from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = {2 * ch for ch in ascii_lowercase}
        print(duplicates)

        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, '')

        return s
