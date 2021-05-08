"""
Synonymous Sentences
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]

"""

from typing import List
from collections import defaultdict

class Solution1:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for synonym_pair in synonyms:
            graph[synonym_pair[0]].append(synonym_pair[1])
            graph[synonym_pair[1]].append(synonym_pair[0])

        synonym_mapping = {}
        synonym_groups = {}
        seen = set()
        accumulating_group_id = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            synonym_mapping[node] = accumulating_group_id
            synonym_groups[accumulating_group_id].add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        # Using a depth-first traversal on the graph to detemine the synonym groups,
        # effectively "coloring" them with a unique identifier as we go
        for char in graph:
            if char in seen:
                continue
            synonym_groups[accumulating_group_id] = set()
            dfs(char)
            accumulating_group_id += 1

        # Sort the synonym groups themselves, so that any subsequent recursion proceeds in the proper sorted order
        for id in synonym_groups:
            words = list(synonym_groups[id])
            words.sort()
            synonym_groups[id] = words

        # Perform recursive sentence building such that every synonym-possible word creates its own recursion tree
        results = []
        split_text = text.split()
        def helper(word_index, running_words):
            if word_index >= len(split_text):
                sentence = " ".join(running_words)
                results.append(sentence)
                return

            word = split_text[word_index]
            if word not in synonym_mapping:
                running_words.append(word)
                helper(word_index+1, running_words)
                running_words.pop()
                return

            synonym_group_id = synonym_mapping[word]
            for synonym in synonym_groups[synonym_group_id]:
                running_words.append(synonym)
                helper(word_index+1, running_words)
                running_words.pop()

        helper(0, [])

        return results

class Solution2:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for s1, s2 in synonyms:
            graph[s1].append(s2)
            graph[s2].append(s1)

        visited = set()
        node_group_map = defaultdict(list)
        group_node_map = defaultdict(list)
        group_id = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            node_group_map[node] = group_id
            group_node_map[group_id].append(node)
            for nei in graph[node]:
                dfs(nei)

        for word in graph:
            if word in visited:
                continue
            dfs(word)
            group_id += 1

        group_node_map = {k: sorted(v) for k, v in group_node_map.items()}

        results = []
        split_text = text.split()

        def helper(word_index, running_words):
            if word_index >= len(split_text):
                sentence = " ".join(running_words)
                results.append(sentence)
                return

            word = split_text[word_index]
            if word not in node_group_map:
                running_words.append(word)
                helper(word_index + 1, running_words)
                running_words.pop()
                return

            synonym_group_id = node_group_map[word]
            for synonym in group_node_map[synonym_group_id]:
                running_words.append(synonym)
                helper(word_index + 1, running_words)
                running_words.pop()

        helper(0, [])

        return results

from collections import deque
from itertools import product
import bisect

class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.parent = {node: node for node in nodes}
        self.rank = {node: 1 for node in nodes}

    def find_parent(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        root_1, root_2 = self.find_parent(node1), self.find_parent(node2)
        if self.rank[root_1] < self.rank[root_2]:
            self.parent[root_1] = root_2
        elif self.rank[root_2] < self.rank[root_1]:
            self.parent[root_2] = root_1
        else:
            self.parent[root_1] = root_2
            self.rank[root_2] += 1

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        syn_word_set = {word for pair in synonyms for word in pair}
        unionFind = UnionFind(syn_word_set)
        for w1, w2 in synonyms:
            unionFind.union(w1, w2)

        group = defaultdict(list)
        for w in syn_word_set:
            bisect.insort(group[unionFind.find_parent(w)], w)

        marked = [w for w in text.split() if w in syn_word_set]
        choices = product(*[group[unionFind.find_parent(w)] for w in marked])
        sentences = []
        for choice in choices:
            lst = deque(choice)
            sentences.append(" ".join([w if w not in syn_word_set else lst.popleft() for w in text.split()]))
        return sentences




synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
print(Solution().generateSentences(synonyms, text))
print(Solution1().generateSentences(synonyms, text))