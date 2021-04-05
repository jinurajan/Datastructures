"""
 Palindrome Permutation II

 Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.



Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
"""
from typing import List

from collections import Counter

from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        result = []
        counter = [0] * 128
        odd_num = 0
        tmp = []
        for char in s:
            counter[ord(char)] += 1
            if counter[ord(char)] % 2 == 0:
                odd_num -= 1
            else:
                odd_num += 1
        if not s or odd_num > 1:
            return result

        for i in range(128):
            if counter[i] % 2 == 1:
                tmp.append(chr(i))
                break

        def backtrack(perm):
            if len(perm) == n:
                result.append("".join(perm[:]))
                return
            for i in range(128):
                if counter[i] > 1:
                    counter[i] -= 2
                    char = chr(i)
                    perm.insert(0, char)
                    perm.append(char)
                    backtrack(perm)
                    counter[i] += 2
                    perm.pop(0)
                    perm.pop()

        backtrack(tmp)
        return result

from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        mid = []
        n = len(s)
        for k, v in counter.items():
            if v % 2 == 1:
                mid.append(k)
        result = []
        if len(mid) <= 1:

            def backtrack(perm):
                if len(perm) == n:
                    result.append(perm)
                    return
                for k, v in counter.items():
                    if v > 1:
                        counter[k] -= 2
                        backtrack(k+perm+k)
                        counter[k] += 2
            backtrack(mid.pop() if mid else "")
        return result


from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        result = []
        n = len(s)
        counter = Counter(s)
        def backtrack(perm):
            if len(perm) == n:
                result.append(perm)
                return
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    backtrack(k+perm+k)
                    counter[k] += 2
        odd_nums = []
        tmp = ""
        for k, v in counter.items():
            if v % 2 == 1:
                odd_nums.append(k)
        if len(odd_nums) > 1:
            return result
        if odd_nums:
            counter[odd_nums[0]] -= 1
            tmp = odd_nums[0]
        backtrack(tmp)
        return result

print(Solution().generatePalindromes("aabb"))
# print(Solution().generatePalindromes("abc"))

print(Solution().generatePalindromes("aabbhijkkjih"))




