"""
Synonymous Sentences
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.


Example 1:

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
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
Example 3:

Input: synonyms = [["a","b"],["c","d"],["e","f"]], text = "a c e"
Output: ["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]
Example 4:

Input: synonyms = [["a","QrbCl"]], text = "d QrbCl ya ya NjZQ"
Output: ["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]


Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[i][0] != synonyms[i][1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.
"""


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for node1, node2 in synonyms:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        node_group_mapping = defaultdict(list)
        group_node_mapping = defaultdict(list)
        group_id = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            node_group_mapping[node] = group_id
            group_node_mapping[group_id].append(node)
            for nei in graph[node]:
                dfs(nei)

        for node in graph:
            if node in visited:
                continue
            dfs(node)
            group_id += 1
        group_node_mapping = {k: sorted(v) for k, v in group_node_mapping.items()}

        result = []
        text = text.split(" ")
        sentence = []

        def helper(index, words):
            if index >= len(text):
                result.append(" ".join(sentence[:]))
                return
            word = words[index]
            if word not in node_group_mapping:
                sentence.append(word)
                helper(index + 1, words)
                sentence.pop()
                return
            # has multiple options
            group_id = node_group_mapping[word]
            for word in group_node_mapping[group_id]:
                sentence.append(word)
                helper(index + 1, words)
                sentence.pop()

        helper(0, text)
        return result


class UnionFind:
	def __init__(self, elements):
		self.elements = elements
		self.parent = {element: element for element in elements}
		self.rank = {element: 1 for element in elements}

	def find(self, x):
		while self.parent[x] != x:
			x = self.parent[x]
		return self.parent[x]

	def union(self, x, y):
		root_x, root_y = self.find(x), self.find(y)
		if self.rank[root_x] < self.rank[root_y]:
			self.parent[root_x] = root_y
		elif self.rank[root_y] < self.rank[root_x]:
			self.parent[root_y] = root_x
		else:
			self.parent[root_x] = root_y
			self.rank[root_y] += 1

class Solution:
	def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
		syn_word_set = {word for pair in synonyms for word in pair}
		unionFind = UnionFind(syn_word_set)

		for w1, w2 in synonyms:
			unionFind.union(w1, w2)

		group = defaultdict(list)
		for w in syn_word_set:
			bisect.insort(group[unionFind.find(w)], w)

		marked = [w for w in text.split() if w in syn_word_set]
		choices = product(*[group[unionFind.find(w)] for w in marked])
		sentences = []
		for choice in choices:
			lst = deque(choice)
			sentences.append(" ".join([w if w not in syn_word_set else lst.popleft() for w in text.split()]))
		return sentencess

class Solution:
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
