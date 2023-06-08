"""
Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are 
sorted lexicographically
 by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.


Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"


Input: words = ["z","x"]
Output: "zx"

# topological sorting ?
1. store indegrees
2. start with characters with 0 indegree and perform dfs 
3. when the indgrees becomes zero add to the result list
4. create a string out of the chars in the result list

"""

from typing import List
from collections import Counter
from collections import defaultdict
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # using bfs for topological sorting
        graph = defaultdict(list)
        indegree = Counter({c:0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c1, c2 in zip(first_word, second_word):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                        indegree[c2] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        output = []
        queue = deque([c for c in indegree if indegree[c] == 0])
        while queue:
            node = queue.popleft()
            output.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(output) < len(indegree):
            return ""
        return "".join(output)

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # using 
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

 


        
        