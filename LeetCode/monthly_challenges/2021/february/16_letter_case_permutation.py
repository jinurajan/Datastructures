"""
Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import List


class Solution1:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [[]]
        for char in S:
            n = len(res)
            if char.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(char.lower())
                    res[n+i].append(char.upper())
            else:
                for i in range(n):
                    res[i].append(char)
        return ["".join(each) for each in res]

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        permutations =['']
        for char in S:
            if char.isalpha():
                permutations = [pref + ch for pref in permutations for ch in (char.lower(), char.upper())]
            else:
                permutations = [pref+char for pref in permutations]
        return  permutations


S = "a1b2"
print(Solution().letterCasePermutation(S))

