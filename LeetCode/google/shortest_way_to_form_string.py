"""
Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.



Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".


Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not source or not target:
            return -1
        char_map = defaultdict(list)
        for idx, num in enumerate(source):
            char_map[num].append(idx)

        pos = -1
        count = 1
        for char in target:
            if char not in char_map:
                return -1
            found = False
            for i in char_map[char]:
                if i > pos:
                    pos = i
                    found = True
                    break
            if not found:
                pos = char_map[char][0]
                count += 1
        return count