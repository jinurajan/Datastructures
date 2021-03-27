"""
Word Subsets

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.


Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from typing import List

from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for word in B:
            for k, c in Counter(word).items():
                d[k] = max(d[k], c) if k in d else c

        result = []
        for word in A:
            a_word_map = Counter(word)
            for k, c in d.items():
                if k not in a_word_map or c > a_word_map[k]:
                    break
            else:
                result.append(word)
        return result

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        b_counter = Counter()
        for b in B:
            b_count = Counter(b)
            for n in b:
                if n in b_counter:
                    b_counter[n] = max(b_counter[n], b_count[n])
                else:
                    b_counter[n] = b_count[n]
        for a in A:
            a_counter = Counter(a)
            valid = True
            for b, count in b_counter.items():
                if b not in a_counter or count > a_counter[b]:
                    valid = False
                    break
            if valid:
                result.append(a)

        return result



