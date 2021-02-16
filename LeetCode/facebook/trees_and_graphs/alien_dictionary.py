"""
Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. If the given input is invalid, return "". If there are multiple valid solutions, return any of them.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
from typing import List

from collections import defaultdict, Counter, deque


class Solution1:
    def alienOrder(self, words: List[str]) -> str:
        """ Using BFS ie queue"""
        adjacency_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        for first, secnd in zip(words, words[1:]):
            for c, d in zip(first, secnd):
                if c != d:
                    if d not in adjacency_list[c]:
                        adjacency_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(secnd) < len(first):
                    return ""
        result = []
        queue = deque([c for c in in_degree if in_degree[c]==0])
        while queue:
            c = queue.popleft()
            result.append(c)
            for d in adjacency_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        if len(result) < len(in_degree):
            return ""
        return "".join(result)

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        reverse_adj_list = {c : [] for word in words for c in word}

        for first, secnd in zip(words, words[1:]):
            for c, d in zip(first, secnd):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:
                if len(secnd) < len(first):
                    return ""
        seen = {}
        result = []
        def visit(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for next_node in reverse_adj_list[node]:
                res = visit(next_node)
                if not res:
                    return False
            seen[node] = True
            result.append(node)
            return True
        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(result)



words = ["wrt","wrf","er","ett","rftt"]
print(Solution().alienOrder(words))
