"""
Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

"""

from collections import defaultdict

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hash_map = defaultdict(int)
        for i, c in enumerate(S):
            hash_map[c] = i
        ans, left, right = [], -1, -1
        for i, c in enumerate(S):
            right = max(right, hash_map[c])
            if i == right:
                # component ended
                ans.append(right - left)
                left = i
        return ans


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = defaultdict(list)
        for idx, char in enumerate(S):
            if char not in d:
                d[char].append(idx)
            else:
                if len(d[char]) == 1:
                    d[char].append(idx)
                else:
                    val = d[char]
                    val[1] = idx
                    d[char] = val
        intervals = list(d.values())
        for interval in intervals:
            if len(interval) == 1:
                interval.append(interval[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return [y - x + 1 for x, y in merged]

