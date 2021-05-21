"""
K-Similar Strings
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Input: s1 = "ab", s2 = "ba"
Output: 1
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Example 3:

Input: s1 = "abac", s2 = "baca"
Output: 2
Example 4:

Input: s1 = "aabc", s2 = "abca"
Output: 2


Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.
"""


class Solution:
    @lru_cache(None)
    def kSimilarity(self, A: str, B: str) -> int:
        if len(A) == 0: return 0  # Base case

        if A[0] == B[0]: return self.kSimilarity(A[1:], B[1:])  # No cost

        for i in range(1, len(B)):
            if B[i] == A[0] and A[i] == B[0]:  # "clean" swap
                return 1 + self.kSimilarity(A[1:i] + A[i + 1:], B[1:i] + B[i + 1:])

        ans = math.inf
        for i in range(1, len(B)):
            if B[i] == A[0]: ans = min(ans, 1 + self.kSimilarity(A[1:], B[1:i] + B[0] + B[i + 1:]))  # Min cost
        return ans
