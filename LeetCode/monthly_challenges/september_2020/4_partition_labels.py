"""
Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

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



print Solution().partitionLabels(S = "ababcbacadefegdehijhklij")
