"""
Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""
from collections import defaultdict

class Solution1:
    def customSortString(self, S: str, T: str) -> str:
        priority_map = {}
        for idx, n in enumerate(S):
            priority_map[n] = idx
        res_map = defaultdict(list)
        rest = ""
        result = ""
        for char in T:
            if char in priority_map:
                res_map[priority_map[char]].append(char)
            else:
                rest += char
        for i in range(len(S)):
            result += ''.join(res_map[i])
        result += rest
        return result

from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count_T = Counter(T)
        ans = ""
        for char in S:
            ans += char * count_T[char]
            count_T[char] = 0
        for char in count_T:
            ans += char * count_T[char]
        return ans
