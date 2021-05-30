"""
Similar String Groups
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.


"""
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def is_similar(word1, word2):
            diff = i = 0
            l = max(len(word1), len(word2))
            while i < l and diff <= 2:
                if word1[i] != word2[i]:
                    diff += 1
                i += 1
            return diff <= 2

        nodes = list(set(strs))
        N = len(nodes)
        d = [i for i in range(N)]
        rank = [0 for i in range(N)]

        def find(a):
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]

        def union(a, b):
            roota, rootb = find(a), find(b)
            if roota != rootb:
                if rank[roota] > rank[rootb]:
                    d[rootb] = roota
                elif rank[rootb] > rank[roota]:
                    d[roota] = rootb
                else:
                    d[roota] = rootb
                    rank[rootb] += 1

        for i in range(N):
            for j in range(i + 1, N):
                if is_similar(nodes[i], nodes[j]):
                    union(i, j)
        return sum([1 for i, e in enumerate(d) if i == e])




